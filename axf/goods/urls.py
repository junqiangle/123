from django.conf.urls import url
from goods import views

urlpatterns = [

    url(r'^$', views.home),
    url(r'register/', views.register,name='register'),
    url(r'login/', views.login ),
]
