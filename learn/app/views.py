from django.shortcuts import render, redirect
from app import models
from hashlib import sha1  # 加密函数


# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        pwd_1 = request.POST.get('cpwd')
        email = request.POST.get('email')
        print(name, pwd, pwd_1, email)
        # 判断 两次输入密码是否一致
        user=models.User.objects.filter(s_name=name).first()
        if pwd_1 == pwd and (not user):
            # 对密码 进行加密
            s1 = sha1()  # 创建加密对象
            s1.update(pwd.encode('utf8'))  # 对密码进行加密
            pwd = s1.hexdigest()  # 返回加密后字符串
            models.User.objects.create(s_name=name, s_pwd=pwd, s_email=email)  # 保存用户
        else:
            return render(request, 'register.html')
        return redirect('/login/')
