# -*- coding: utf-8 -*-
# encoding = utf-8


'''
    此种方式是在自己的MySQL安装路径下面产生创建的数据库的文件夹
    并不是在当前的python工程路径下创建了.sql文件
'''
# 导入数据库模块
import MySQLdb

# 连接数据库
conn = MySQLdb.connect(host='localhost', user='root', passwd='root', port=3306)

# 获取操作游标
cursor = conn.cursor()

# 创建数据库
cursor.execute('create database if not exists dutylist')

# 选择数据库
conn.select_db('dutylist')

# 创建表
cursor.execute('create table if not exists du_category(category_id int, name varchar(64))')
cursor.execute('create table if not exists du_duty(duty_id int, category_id int, user_id int, title varchar(64), '
               'status int, is_show int, create_time int)')
cursor.execute('create table if not exists du_user(user_id int, username varchar(64), phone varchar(64), '
               'password varchar(64), create_time int)')
conn.commit()

# 写信息到表中方式1
cursor.execute("insert into du_category(category_id, name) values(1234567, 'hello world')")
conn.commit()

# 写信息到表中方式2，需要注意的是不论是些什么数据类型都是需要用%s来表示
cursor.execute('insert into du_category(category_id, name) values(%s, %s)', (7654321, "world hello"))
conn.commit()

# 使用方式2同时写入多条信息
cursor.executemany('insert into du_category(category_id, name) values(%s, %s)', ((123, "hello"), (456, "world"),
                   (789, "python")))
conn.commit()

# 刪除表中指定列的信息
cursor.execute('delete from du_category where name = "hello world"')
conn.commit()

# 获取表的信息，获取的信息列表中没有字段信息，需要手动输入
cursor.execute('select * from du_category')
information = cursor.fetchall()
for info in information:
    print 'category_id: %d; name: %s' % (info[0], info[1])

cursor.execute('delete from du_category where category_id = 123')
conn.commit()

# 更新信息
cursor.execute('update du_category set name = "magic" where category_id = 456')
conn.commit()

cursor.execute('delete from du_category')
conn.commit()

# 获取表的信息，列表中包含字段信息
cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
cursor.execute('select * from du_category')
information = cursor.fetchall()
for info in information:
    print info

cursor.close()
conn.close()
