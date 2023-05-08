from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path("item/", views.todo_main, name='todo_main'),
]