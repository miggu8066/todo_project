from django.shortcuts import render, redirect
from .models import User
from django.db import transaction
from argon2 import PasswordHasher
from .forms import RegisterFrom, LoginForm

def register(request):
    register_form = RegisterFrom()
    context = {'forms' : register_form}

    if request.method == 'GET':
        return render(request, 'user/register.html', context)
    
    elif request.method == 'POST':
        register_form = RegisterFrom(request.POST)
        if register_form.is_valid():
            user = User(
                user_id = register_form.user_id,
                user_pw = register_form.user_pw,
                user_name = register_form.user_name,
                user_email = register_form.user_email
            )
            user.save()
            return redirect('/')
        else:
            context['forms'] = register_form   ##이해가 안돼는 부분
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error'] = value
        return render(request, 'user/register.html', context)

def login(request):
    loginform = LoginForm()
    context = { 'forms' : loginform}

    if request.method == 'GET':
        return render(request, 'user/login.html', context)
    
    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            return redirect('/')
        else:
            context['forms'] = loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request, 'user/login.html', context)