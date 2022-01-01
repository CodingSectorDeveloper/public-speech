from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login as _login, logout as _logout, authenticate as _authenticate
from .models import *

def index(request):
    news = News.objects.all()
    return render(request, "index.html", {"news":news})

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = _authenticate(username=username, password=password)
        if user is not None:
            _login(request, user)
            return HttpResponseRedirect("/")
        else:
            context = {
                'error': True,
                'message': 'Invalid Credentials'
            }
            return render(request, "login.html", context)
    context = {

    }
    return render(request, "login.html", context)

def logout(request):
    _logout(request)
    return HttpResponseRedirect("/")

def news_details(request, id):
    news = News.objects.filter(pk=id).last()
    more_news = News.objects.all()
    print(more_news)
    more_news = more_news.exclude(pk=id)
    return render(request, "news_details.html", {"news":news, "more_news":more_news})

def dashboard(request):
    if request.user.is_superuser:
        return HttpResponseRedirect("/admin_dashboard")

def contact(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        message = request.POST['message']
        message_created = Message.objects.create(full_name=full_name, email=email, message=message)
        return render(request, "contact.html", {"success":True})
    return render(request, "contact.html")