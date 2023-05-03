from django import forms
from .models import Todo_list

class TodoItemsForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        field = ['todo_content']
    
    todo_content = forms.CharField(

    )
