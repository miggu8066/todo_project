from django.shortcuts import render, HttpResponse
from user.models import User

def main_page(request):
    context = {}

    login_session = request.session.get('login_session','')

    if login_session == '':
        context['login_session'] = False
    else:
        context['login_session'] = True
    
    return render(request, 'firstapp/index.html', context)
