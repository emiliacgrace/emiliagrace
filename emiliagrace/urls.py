from django.urls import path
from blog import views
from blog.admin import admin_site

urlpatterns = [
    path('', views.home),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path("admin/", admin_site.urls),
]
