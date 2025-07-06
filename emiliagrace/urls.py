from django.urls import path
from django.contrib import admin
from blog import views as blog_views
from schedule_viewer import views as svsv_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('post/<slug:slug>/', blog_views.blog_detail, name='blog_detail'),
    path('svsv', svsv_views.svsv_home, name='svsv_home'),
    path("admin/", admin.site.urls),
]
