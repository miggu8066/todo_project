from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path("RegisterAndLogin/", views.RegisterAndLogin, name='RegisterAndLogin'),
    path("logout/", views.logout, name='logout'),
]