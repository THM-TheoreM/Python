#coding=utf-8
import MySQLdb

print u'-----插入数据-----'
username=''
password=''
databasename=''
db=MySQLdb.connect('localhost',username,password,databasename)
cursor=db.cursor()
sql='''insert into employee(first_name,last_name,age,sex,income) values('mac','mohan',20,'m',2000)'''
cursor.execute(sql)
db.close()