from django.shortcuts import redirect, reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


class SignUpView(CreateView):
    template_name = 'market_user_forms/signup.html'
    form_class = SignUpForm
    success_message = "Your profile was created successfully"

    success_url = '/user/signin/'


def sign_in(request):

    form = SignInForm(request.POST or None)
    context = {
        "form": form
    }
    if request.user.is_authenticated:
        return redirect('posts')
    if form.is_valid():
        email = form.cleaned_data.get("email_login")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            
            messages.success(request, 'وارد شدید!')
            return redirect(reverse('panel'))
        else:
            messages.success(request, 'your password is not correct!')
    return render(request, "market_user_forms/signin.html", context)
