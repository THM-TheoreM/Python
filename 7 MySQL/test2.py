#coding=utf-8
import MySQLdb

print u'-----创建表-----'
username=''
password=''
databasename=''
db=MySQLdb.connect('localhost',username,password,databasename)
cursor=db.cursor()
sql='''create table employee(
       first_name char(20) not null,
	   last_name char(20),
	   age int,
	   sex char(1),
	   income float)'''
cursor.execute(sql)
db.close()