#coding=utf-8 

'''
   set 集合
'''

e={'a',7,'b',8}
f=set(['a',7,'b',8])
if e==f:
	print True

print len(e)
print e

e.add(4)
print e
e.remove('b')
print e

f=set([1,2,8])
print e & f
print e | f
print e - f

for x in e:
	print x
for x in range(len(e)):
	print x