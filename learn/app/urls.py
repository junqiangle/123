from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'login/', views.login),
    url(r'register',views.register),# 配置url地址

]
