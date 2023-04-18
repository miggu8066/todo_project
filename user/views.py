from django.shortcuts import render, redirect
from .models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    
    elif request.method == 'POST':
        user_id = request.POST.get('id','')
        user_pw = request.POST.get('pw','')
        user_pw_confirm = request.POST.get('pw-confirm','')
        user_name = request.POST.get('name','')
        user_email = request.POST.get('email','')

        if (user_id or user_pw or user_pw_confirm or user_name or user_email) == '':
            return redirect('/user/register')
        elif user_pw != user_pw_confirm:
            return redirect('/user/register')
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name,
                user_email = user_email,
            )
            user.save()
        return redirect('http://127.0.0.1:8000/main/')