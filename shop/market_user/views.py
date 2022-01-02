from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import FormView, View
from .forms import SignUpForm, SignInForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages
 
class SignUpView(CreateView):
    template_name = 'market_user_forms/signup.html'
    form_class = SignUpForm
    success_message = "Your profile was created successfully"
    
    success_url = '/user/signin/'
    
    # def post(self, request, *args, **kwargs):
    #     print('post is post')
    #     return redirect('posts')
    # def form_valid(self, form):
    #     print('-------------------------------------')
    #     return redirect('posts')


# class SignInView(FormView):
#     template_name = 'market_user_forms/signin.html'
#     form_class = SignInForm
#     success_url ="/post/posts"
    
    
    # def get_success_url(self):
    #     return reverse_lazy('posts')
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     if self.request.user.is_authenticated:
    #         return redirect('posts')
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         return redirect('posts')
    #     print(request.uesr)
    #     return render(request, self.template_name, {'form': form})


def sign_in(request):
    form = SignInForm(request.POST or None)
    context = {
        "form": form
    }
    if request.user.is_authenticated:
        return redirect('posts')
    if form.is_valid():
        email  = form.cleaned_data.get("email_login")
        password  = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            print(user)
            login(request,user)
            messages.success(request, 'وارد شدید!')
            return redirect(reverse('posts'))
        else :
            messages.success(request, 'your password is not correct!')
    return render(request, "market_user_forms/signin.html", context)
    


# def signup(request):
#     form = SignUpForm(None or request.POST)
#     if request.method == "POST":
#         print('postform')
#         if form.is_valid():
#             print('formisvalid')
#             user = CustomUser.objects.create_user(phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'], password=form.cleaned_data['password'],
#                                                   first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], user_type_owner_shop=form.cleaned_data['user_type_owner_shop'])
#             print('new user register is :', user)
#             print('----')
#             return redirect('posts')

#     return render(request, 'market_user_forms/signup.html', {'form': form})
