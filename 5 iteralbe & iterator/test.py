#coding=utf-8
from collections import Iterable
from collections import Iterator


class F:
	def __init__(self):
		self.a, self.b = 0,1
		
class H:
	def __init__(self):
		self.a, self.b = 0,1
	
	def __iter__(self):
		return self
		

class Fib:
	def __init__(self):
		self.a, self.b = 0,1
		
	def __iter__(self):
		return self
		
	def next(self):
		self.a,self.b = self.b,self.a+self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
		
def f():
	print 1
	
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1
		
'''
Non-Iterable:类的内部没有实现Iterable，即__iter__
'''
a=F()
print isinstance(a,Iterable)
a=f
print isinstance(a,Iterable)
print '\n'

'''
Iterable:类的内部实现了Iterable，即__iter__
'''
print isinstance('abc',Iterable)
print isinstance('abc',Iterator)
print isinstance([],Iterable)
print isinstance([],Iterator)
print isinstance((),Iterable)
print isinstance((),Iterator)
print isinstance({'one':'one'},Iterable)
print isinstance({'one':'one'},Iterator)
print isinstance({1,2},Iterable)
print isinstance({1,2},Iterator)
print '\n'

a=H()
print isinstance(a,Iterable)
print isinstance(a,Iterator)
print '\n'

'''
Iterator:类的内部不仅实现了Iterable，即__iter__，也实现了Iterator，即next
'''
print isinstance((x for x in range(11)),Iterable)
print isinstance((x for x in range(11)),Iterator)
print '\n'

a=fib(6)
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=Fib()
print isinstance(a,Iterable)
print isinstance(a,Iterator)



