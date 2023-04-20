from django.shortcuts import render, redirect
from .models import User
from django.db import transaction
from argon2 import PasswordHasher
from .forms import RegisterFrom

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
    
# def register(request):
#     if request.method == 'GET':
#         return render(request, 'user/register.html')
    
#     elif request.method == 'POST':
#         user_id = request.POST.get('id','')
#         user_pw = request.POST.get('pw','')
#         user_pw_confirm = request.POST.get('pw-confirm','')
#         user_name = request.POST.get('name','')
#         user_email = request.POST.get('email','')

#         if (user_id or user_pw or user_pw_confirm or user_name or user_email) == '':
#             return redirect('/user/register')
#         elif user_pw != user_pw_confirm:
#             return redirect('/user/register')
#         else:
#             user = User(
#                 user_id = user_id,
#                 user_pw = user_pw,
#                 user_name = user_name,
#                 user_email = user_email,
#             )
#             user.save()
#         return redirect('http://127.0.0.1:8000/main/')