from django.shortcuts import redirect
from .models import User

def login_required(func):
    