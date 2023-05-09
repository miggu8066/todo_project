from django import forms
from .models import Todo_list

class TodoItemsForm(forms.ModelForm):
    class Meta:
        model = Todo_list
        exclude = ['writer']
    
    todo_content = forms.CharField(
        max_length=225,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'TODAY_ITEM'
            }
        ),
    )

    field_order = [
        'todo_content'
    ]
    
    def clean(self):
        cleaned_data = super().clean()

        todo_content = cleaned_data.get('todo_content', '')

        if todo_content == '':
            self.add_error('todo_content', '내용을 입력하세요')
        else:
            self.todo_content = todo_content

class TodoDeleteForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Todo_list
        fields = ('id',)