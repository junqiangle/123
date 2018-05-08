'''
__init__：没有参数，在服务器响应的第一个请求的时候自动调用，用户确定时候启动该中间件

process_request(self, request): 在执行视图前被调用，每个请求上都会被调用，不主动进行返回或返回HttpResponse对象(常用)

process_view(self, request, view_func,view_args, view_kwargs):调用视图之前执行，每个请求都会调用，不主动进行返回或返回HttpResponse对象

process_template_response(self, request, response)：在视图刚好执行完后进行调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象

process_response(self, request, response):所有响应返回浏览器之前调用，每个请求都会调用，不主动进行返回或返回HttpResponse对象
process_exception(self, request, exception):当视图抛出异常时调用，不主动进行返回或返回HttpResponse对象

'''

import time
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin # 中间键方法
from goods.models import TicketModel # 导入自己创建的cookie模块


class authmiddleware(MiddlewareMixin):
    def process_request(self, request):
        ticket = request.COOKIES.get('cook')
        if not ticket:
            pass  # 假如 自己的cook 模块为空时 直接去寻找视图函数
        else:
            user = TicketModel.objects.filter(ticket=ticket).first()
            if user:
                if int(time.time()) >= user.out_time: # 对自设的cook值进行有效时间判断
                    user.delete()
                    return HttpResponseRedirect('/login/')
                else:
                    print(1)
                    request.user = user.u_id
                    print(user.u_id)
