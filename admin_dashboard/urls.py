from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add_news/', views.add_news, name="add_news"),
    path('news/', views.news, name="news"),
    path('news_details/<int:id>', views.news_details, name="news_details"),
    path('news_delete/<int:id>', views.news_delete, name="news_delete"),
    path('messages/', views.messages, name="messages"),
    path('message_details/<int:id>', views.message_details, name="message_details"),
]
