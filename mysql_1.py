#-*-coding:utf-8 -*-
import redis
# 连接redis 库
db = redis.Redis(
    host='47.106.98.155',
    port='10086'
)
# 获取redis 库里的数据  数据是字典形式
db_user=db.hgetall('user')
# y =y.decode('utf8')
# 对字典的值解码并输出
for key in db_user:
    key = db_user[key]
    key=key.decode()
    print(key,end='\t')
