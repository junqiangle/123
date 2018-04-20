# -*-coding;utf-8-*-
import pymysql

# 连接数据库
db = pymysql.connect(
    host='47.106.98.155',
    user='root',
    passwd='123456',
    db='hr',
    charset='utf8',
    port=3306
)
sel = '''delete from s where passwd=1233'''
# 把表缓存在内存中
x = db.cursor()
# 执行mysql 语句
x.execute(sel)
#  插入数据需要提交才能在数据库跟新
db.commit()
sel_1 = '''select * from s'''
x.execute(sel_1)
y = x.fetchall()
print(y)
# 关闭数据库
db.close()
