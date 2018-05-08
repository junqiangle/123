import time
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from goods.models import *
# from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse
from utils.cook import cookie


# Create your views here.
def home(request):
    '''
    对首页视图函数定义
    :param request: 前端 来的数据
    :return:  返回给前端文件
    '''
    wheel = MainWheel.objects.all()
    main_nav = MainNav.objects.all()
    must_buy = Mainmustbuy.objects.all()
    # main_shops_1 = MainShop.objects.all()[0] 切片操作
    # main_shops_2 = MainShop.objects.all()[1:3]
    # main_shops_3 = MainShop.objects.all()[3:7]
    # main_shops_4 = MainShop.objects.all()[7:11]
    main_show = MainShow.objects.all()
    shops = MainShop.objects.all()  # html筛选操作
    data = {'wheels': wheel,
            'main_navs': main_nav,
            'must_buys': must_buy,
            # 'shop_1': main_shops_1,   切片操作
            # 'shop_2': main_shops_2,
            # 'shop_3': main_shops_3,
            # 'shop_4': main_shops_4,
            'main_show': main_show,
            'shops': shops
            }
    return render(request, 'home/home.html', data)


def register(request):
    '''
    注册页面函数
    :param request:
    :return: 假如是get请求是返回原页面 假如是POST请求重定向时登录页面
    '''
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        # file = request.POST.get('icon')
        file = request.FILES.get('icon') # 获取图片 得先安装Pillow 文件包
        print(file)

        # s1=sha1()
        # s1.update(pwd.encode('utf8'))  对密码进行加密
        # pwd =s1.hexdigest()
        print(name, pwd, email, file, end='\t')
        pwd = make_password(pwd)

        UserModel.objects.create(username=name, password=pwd, email=email, icon=file) # 对用户名 等保存
        return redirect('axf:login')


def login(request):
    '''
    登录函数
    :param request:
    :return: 假如是get请求返回登录页面  假如入postQ请求 先判断是否有此用户
    有此用户在设置cookie值 在重定向到mine页面
    '''
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = UserModel.objects.filter(username=name)
        username = user.count()
        if username == 1:  # 判断用户是否存在
            if check_password(pwd, user[0].password):  # 对密码核对
                cook = cookie()  # 产生一个随机cookie值
                response = HttpResponseRedirect('/mine/')
                response.set_cookie('cook', cook, max_age=3000)  # 设置cookie值
                outtime = int(time.time()) + 3000
                user = user[0].id
                print(user)
                TicketModel.objects.create(ticket=cook, out_time=outtime, u_id_id=user) #对用户cookie保存

                return response
            else:
                return render(request, 'user/user_login.html')
        else:
            return render(request, 'user/user_login.html')


# def name(request):
#     user=request.GET.get('username')
#     status=UserModel.objects.filter(username=user).count()
#     if status==1:
#         date={'status':200}
#         return JsonResponse(date)
def mine(request):
    return render(request, 'mine/mine.html')


# def login(request):
#     if request.method == 'GET':
#         return render(request, 'user/user_login.html')
#     if request.method == 'POST':
#         user = request.POST.get('username')
#         password = request.POST.get('password')
#         users = UserModel.objects.filter(username=user, is_delete=0).exists()
#         if users:
#             User = UserModel.objects.get(username=user)
#             if check_password(password, User.password):
#                 s = '1234567890qwertyuiopasdfghjklzxcvbnm'
#                 ticket = ''
#                 for i in range(15):
#                     ticket += random.choice(s)
#                 ticket += str(int(time.time()))
#                 outtime = int(time.time()) + 3000
#                 isexists = UserLogin.objects.filter(user=User.id).exists()
#                 if isexists:
#                     userlogin = UserLogin.objects.get(user=User)
#                     userlogin.ticket = ticket
#                     userlogin.out_time = outtime
#                     userlogin.save()
#                 else:
#                     UserLogin.objects.create(
#                         user=User,
#                         ticket=ticket,
#                         out_time=outtime,
#                     )
#                 path = request.GET.get('path')
#                 if path == None:
#                     path = 'cart'
#                 response = HttpResponseRedirect('/app/%s' % path)
#                 # response.set_cookie('ticket', ticket, expires='过期日期')
#                 response.set_cookie('ticket', ticket, max_age=3000)
#                 return response
#             else:
#                 return render(request, 'user/user_login.html')
#         else:
#             return render(request, 'user/user_login.html')

def delete(request):
    '''
    对页面中 退出针对函数
    :param request:
    :return:  删除此次用户登录的设置的cookie值 并返回mine 重新渲染页面
    '''
    print(request.user)
    u = request.user.id  #
    c = TicketModel.objects.filter(u_id_id=u).delete()  # 退出时删除cook
    return redirect('/mine/')
