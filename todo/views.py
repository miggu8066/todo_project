from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from todo.forms import TodoItemsForm, TodoDeleteForm
from .models import Todo_list
from user.models import User
from user.decorators import login_required

@login_required
def todo_main(request):
    login_session = request.session.get('login_session', '')
    
    if request.method == 'GET':
        todo_list = Todo_list.objects.filter(writer__user_id=login_session)
        context = {
            'todo_list': todo_list,
            'login_session': login_session,
            'Items': TodoItemsForm(),
            'DeleteForm' : TodoDeleteForm()
        }
        return render(request, "todo/todo_list.html", context)
    
    elif request.method == 'POST':
        if 'add_todo' in request.POST:
            Itemsform = TodoItemsForm(request.POST)

            if Itemsform.is_valid():
                writer = User.objects.get(user_id=login_session)
                todo_list = Todo_list(
                    writer = writer,
                    todo_content = Itemsform.cleaned_data['todo_content'],
                )
                todo_list.save()
                return redirect('/todo/item/')
            else:
                context = {
                    'Items': Itemsform,
                    'login_session': login_session,
                }
                if Itemsform.errors:
                    for value in Itemsform.errors.values():
                        context['error'] = value
                return render(request, "todo/todo_list.html", context)
        
        elif 'delete_todo' in request.POST:
            DeleteForm = TodoDeleteForm(request.POST)

            if DeleteForm.is_valid():
                if 'checkbox' in request.POST:
                    todo_id = DeleteForm.cleaned_data['id']
                    Todo_list.objects.filter(id=todo_id).delete()
                    return redirect('/todo/item/')
                else:
                    context = {
                        'Items': TodoItemsForm(),
                        'DeleteForm': TodoDeleteForm(),
                        'login_session': login_session,
                        'error': '체크박스를 선택하세요.'
                    }
                    if DeleteForm.errors:
                        context['error'] = DeleteForm.errors.as_text()
                    return render(request, "todo/todo_list.html", context)
            else:
                context = {
                    'Items': TodoItemsForm(),
                    'DeleteForm': DeleteForm,
                    'login_session': login_session,
                    'error': DeleteForm.errors.as_text()
                }
                return render(request, "todo/todo_list.html", context)

        elif 'delete_all' in request.POST:
            todo_list = Todo_list.objects.filter(writer__user_id=login_session)
            todo_list.delete()
            return redirect('/todo/item/')
        
@login_required
def update_todo(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        new_text = request.POST.get('new_text')

        try:
            todo_item = Todo_list.objects.get(id=item_id, writer__user_id=request.session.get('login_session'))
            todo_item.todo_content = new_text
            todo_item.save()
            return JsonResponse({'success': True})
        except Todo_list.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Todo item not found.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})