from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect

from .models import User

def sign_up(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print('User created:', user)

            return redirect('log-in')
    #     else:
    #         print('Somethign went wrong')
    # else:
    #     print('Just show the form!')

    return render(request, 'account/sign-up.html')

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password1', '')

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request, 'core/index.html')
    return render(request,'account/log-in.html',)

def log_out(request):
    if request.user:
        auth_logout(request)
    
    return redirect('/')
