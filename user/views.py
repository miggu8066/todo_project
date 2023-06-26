from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from user.decorators import login_required
from .models import User
from django.db import transaction
from argon2 import PasswordHasher
from .forms import RegisterFrom, LoginForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

@login_required
def Myinfo(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    user = User.objects.get(user_id=login_session)

    context = {
        'user_name': user.user_name,
        'user_email': user.user_email,
        'user_id': user.user_id,
    }

    return render(request, 'user/myinfo.html', context)


def RegisterAndLogin(request):
    loginforms = LoginForm()
    registerforms = RegisterFrom()
    context = { 'loginforms' : loginforms,
               'registerforms' : registerforms,}

    if request.method == 'GET':
        return render(request, 'user/login.html', context)
    
    elif 'login' in request.POST:
        loginforms = LoginForm(request.POST)

        if loginforms.is_valid():
            request.session['login_session'] = loginforms.login_session
            request.session.set_expiry(0)
            return redirect('/')
        else:
            context['loginforms'] = loginforms
            
            if loginforms.errors:
                for login_value in loginforms.errors.values():
                    context['login_error'] = login_value
        return render(request, 'user/login.html', context)
    
    elif 'register' in request.POST:
        registerforms = RegisterFrom(request.POST)

        if registerforms.is_valid():
            user = User(
                user_id = registerforms.user_id,
                user_pw = registerforms.user_pw,
                user_pw_confirm = registerforms.user_pw_confirm,
                user_name = registerforms.user_name,
                user_email = registerforms.user_email,
            )
            user.save()
            return redirect('/user/RegisterAndLogin/')
        else:
            context['registerforms'] = registerforms

            if registerforms.errors:
                for register_value in registerforms.errors.values():
                    context['registerforms_error'] = register_value
        return render(request, 'user/login.html', context)
    
def logout(request):
    request.session.flush()
    return redirect('/')