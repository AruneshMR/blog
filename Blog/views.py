from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
# Create your views here.


def addblog(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.FILES['myaudio']:
        author = request.user
        title = request.POST['title']
        story = request.POST['story']
        img = request.FILES['myfile']
        myaudio = request.FILES['myaudio']
        published_date = timezone.now()
        Bolgs.objects.create(author=author, title=title, story=story, img=img, audio=myaudio, published_date=published_date)
        print('added blog')
        return redirect('home')
    else:
        return render(request, 'blog_pages/addBlog.html')


def liblogs(request):
    data = Bolgs.objects.filter(author=request.user)
    return render(request, 'blog_pages/listBlog.html', {'data': data})


def csv(request):
    pass


def pdf(request):
    pass


def viewblog(request):
    return render(request, 'blog_pages/viewblog.html')
