from django.urls import path
from firstapp import views

urlpatterns = [
    path("main2", views.index),
]
