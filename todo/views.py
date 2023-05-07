from django.shortcuts import render, redirect
from todo.forms import TodoItemsForm
from .models import Todo_list
from user.models import User
from user.decorators import login_required

@login_required
def todo_main(request):
    login_session = request.session.get('login_session', '')
    context = { 'login_session' : login_session }

    if request.method == 'GET':
        Itemsform = TodoItemsForm()
        context['Items'] = Itemsform
        todo_list = Todo_list.objects.all()
        context['todo_list'] = todo_list
        return render(request, "todo/todo_list.html", context)
    
    elif request.method == 'POST':
        Itemsform = TodoItemsForm(request.POST)

        if Itemsform.is_valid():
            writer = User.objects.get(user_id=login_session)
            todo_list = Todo_list(
                writer = writer,
                todo_content = Itemsform.cleaned_data['todo_content']
            )
            todo_list.save()
            return redirect('/todo/')
        else:
            context['Items'] = Itemsform
            if Itemsform.errors:
                for value in Itemsform.errors.values():
                    context['error'] = value
            todo_list = Todo_list.objects.all()
            context['todo_list'] = todo_list
            return render(request, "todo/todo_list.html", context)