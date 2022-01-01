from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('news_details/<int:id>', views.news_details, name="news_details"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
