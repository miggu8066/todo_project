from django.shortcuts import render, redirect
from .models import Todo_list
from user.models import User

def todo_main(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    return render(request, "todo/todo_list.html", context)