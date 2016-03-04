#coding=utf-8
from collections import Iterable
from collections import Iterator
 
a=[x for x in range(11)]
print a

a=(x for x in range(11))
print isinstance(a,Iterable)
print isinstance(a,Iterator)
print '\n'
print next(a)
print next(a)
print '\n'
for x in a:
	print x

	
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3
print isinstance(a,Iterable)
print isinstance(a,Iterator)	
a=odd()
for x in a:
	print x

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=fib(6)
for x in a:
	print x
	
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

a=iter('abc')
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=iter([])
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=iter(())
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=iter({'one':'one'})
print isinstance(a,Iterable)
print isinstance(a,Iterator)
a=iter({1,2})
print isinstance(a,Iterable)
print isinstance(a,Iterator)

a='python'   #字符串，非惰性，不是生成器
for x in a:
	print x
print '\n'
for x in a:   #这里还有'python'
	print x
print '\n'

a=iter(a)   #不是字符串，惰性，是迭代器（上面的生成器是迭代器的特殊形式）
for x in a:
	print x
for x in a:   #这里没有'python'
	print x