from django.conf.urls import url
from goods import views

urlpatterns = [

    url(r'^$', views.home),
    url(r'register/', views.register,name='register'),#注册
    url(r'login/', views.login,name='login'),#登录
    url(r'mine/',views.mine,name='mine'),
    url(r'^del$',views.delete,name='del')

]
