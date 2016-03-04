#coding=utf-8 

'''
   dict 字典
'''

a={'one':'a','two':7,'three':'b','four':8}
print len(a)
print a
print a['one']
print a.keys()
print a.values()

a['one']=1
print a
del a['one']
print a
a.pop('four')
print a
a.pop('three')
print a

for x in a:
	print x
for x in range(len(a)):
	print x
for x,y in a.items():
	print x,y

