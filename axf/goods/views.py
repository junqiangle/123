from django.shortcuts import render
from goods.models import *


# Create your views here.
def home(request):
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
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method=='POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        file = request.POST.get('icon')
        print(name, pwd, email, file)
    return render(request, 'user/user_register.html')


def login(request):
    pass
