#coding=utf-8 

'''
   tuple 元组
1. 不可变对象
'''

a=('a',7,'b',8)
print len(a)
print a
print a[0]
print a*2
print a+('c',)

for x in a:
	print x
for x in range(len(a)):
	print x
	
a=tuple(range(1,11))
print a