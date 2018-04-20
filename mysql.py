
import pymysql
'''
连接阿里云服务器里的database，host为ip地址
选择database名字为 SRS，端口默认为3306
'''
db = pymysql.Connect(host='47.106.98.155',
                     user='root',
                     passwd='123456',
                     db='HR',
                     port=3306,
                     charset='utf8')

print(db)
# 3 获取游标--》 开辟的一个缓冲区，用于放sql 语句执行结果
cursor =db.cursor()
sel ='select * from dept'
s
print(sel)
db.close()
# 查询游标
# cursor = db.cursor()
# # 执行sql
# sql = 'select*from dept;'
# cursor.execute(sql)
#
# # 获取结果
# data = cursor.fetchall()
#
#
#
# # 关闭连接
