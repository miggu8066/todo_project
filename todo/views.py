from django.shortcuts import render, redirect
from todo.forms import TodoItemsForm
from .models import Todo_list
from user.models import User
# from user.decorators import login_required

# @login_required
def todo_main(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    if request.method == 'GET':
        Itemsform = TodoItemsForm()
        context['Items'] = Itemsform
        
        return render(request, "todo/todo_list.html", context)