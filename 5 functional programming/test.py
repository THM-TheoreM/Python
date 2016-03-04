#coding=utf-8
from functools import reduce

def f(x):
	return x*x
	
a=map(f,[1,2,3])   #迭代器
a=list(a)          #list
print a


def is_odd(n):
    return n%2 == 1
	
a=filter(is_odd,[1,2,3,4,5,6,7])   #迭代器
a=list(a)                          #list
print a

def add(x,y):
	return x+y

a=reduce(add, [1, 3, 5, 7, 9])
print a

a=sorted(['bob', 'about', 'Zoo', 'Credit'])
print a

a=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)
print a

a=sorted(['bob', 'about', 'Zoo', 'Credit'],reverse=True)
print a

a=sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)
print a

a=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

def by_name(t):
	return t[0]
b=sorted(a,key=by_name)
print b

def by_score(t):
	return t[1]
b=sorted(a,key=by_score)
print b

