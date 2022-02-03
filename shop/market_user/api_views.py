from rest_framework import generics, status
from .models import *
from rest_framework.response import Response
from .serializers import *
from . import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpApi(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializers


class UserList(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get_object(self):
        print(self.request.user)
        return CustomUser.objects.get(email=self.request.user)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class OTPView(APIView):
    def get(self, request):
        serializer = serializers.RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            try:
                otp = OTPRequest.objects.generate(data)
                return Response(data=serializers.RequestOTPResponseSerializer(otp).data)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)
    def post(self, request):
        serializer = serializers.VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                return Response(self._handle_login(data))
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)

    def _handle_login(self, otp):
        query = CustomUser.objects.filter(phone_number=otp['receiver'])
        if query.exists():
            created = False
            user = query.first()
        else:
            user = CustomUser.objects.create(phone_number=otp['receiver'] )
            created = True

        refresh = RefreshToken.for_user(user)

        return serializers.ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created':created
        }).data
