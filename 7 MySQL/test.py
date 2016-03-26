#coding=utf-8
import MySQLdb

print u'-----创建数据库-----'
username=''
password=''
databasename=''
db=MySQLdb.connect('localhost',username,password,databasename)
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print 'database version: %s' % data
db.close()