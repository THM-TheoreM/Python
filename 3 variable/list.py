#coding=utf-8 

'''
   list 列表
1. 可变对象
'''

a=['a',7,'b',8]
print len(a)
print a
print a[0]
print a*2
print a+['c']

a[0]=1
print a
del a[0]
print a
a.append('c')
print a
a.insert(0,2)
print a
a.pop()
print a
a.pop(0)
print a

for x in a:
	print x
for x in range(len(a)):
	print x
	
a=list(range(1,11))
print a
a=[]
for x in range(1,11):
	a.append(x)
print a
a=[x for x in range(1,11)]
print a