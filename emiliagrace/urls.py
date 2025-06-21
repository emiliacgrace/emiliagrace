from django.urls import path
from django.contrib import admin
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path("admin/", admin.site.urls),
]
