from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path("item/", views.todo_main, name='todo_main'),
    path("update/", views.update_todo, name='update_todo'),
]