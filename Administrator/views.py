from django.shortcuts import render, redirect
from .models import *

from Blog.models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def index(request):
    return render(request, 'html_pages/index.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                         last_name=last_name)
                print('user created')
                return redirect('signin')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup')
    else:
        return render(request, 'html_pages/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')


        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'html_pages/signin.html', context)
    else:

        return render(request, 'html_pages/signin.html')


def logout(request):
    auth.logout(request)
    return render(request, 'html_pages/signin.html')


def home(request):
    updates = User.objects.get(username=request.user)
    try:
        get2 = UserProfile.objects.get(user=updates)
    except:
        get2 = ' '
    if request.user.is_superuser:
        print(request.user)
        return render(request, 'html_pages/admin.html', {'datas': get2})
    else:
        print(request.user)

        return render(request, 'html_pages/home.html', {'datas': get2})


def authors(request):
    data = User.objects.all()
    return render(request, 'html_pages/authors.html', {'data': data})


def adbloglist(request):
    listdata = Bolgs.objects.all()
    return render(request, 'html_pages/adlistblog', {'listdata': listdata})
