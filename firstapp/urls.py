from django.urls import path
from firstapp import views

app_name = 'todo_main'
urlpatterns = [
    path("", views.main_page, name='main_page'),
]