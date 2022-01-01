from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from main.models import *

def index(request):
    return render(request, "Admin/home.html", {"newsnum": len(News.objects.all())})

def add_news(request):
    if request.method == 'POST':
        news_title = request.POST['news_title']
        news_description = request.POST['news_description']
        news_thumbnail = request.FILES['news_thumbnail']
        news_video = request.FILES['news_video']
        news_created = News.objects.create(title=news_title, description=news_description, thumbnail=news_thumbnail, video=news_video, uploaded_by=request.user)
        return render(request, "Admin/add_news.html", {"success":True})
    return render(request, "Admin/add_news.html")

def news(request):
    return render(request, "Admin/news.html", {"news":News.objects.all()})

def news_details(request, id):
    return render(request, "Admin/news_details.html", {"news":News.objects.filter(pk=id).last()})

def news_delete(request, id):
    News.objects.filter(pk=id).last().delete()
    return HttpResponseRedirect("/admin_dashboard/news")

def messages(request):
    messages = Message.objects.all()
    print(messages)
    return render(request, "Admin/messages.html", {"messages":messages})

def message_details(request, id):
    return render(request, "Admin/message_details.html", {"message":Message.objects.filter(pk=id).last()})