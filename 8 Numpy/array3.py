#encoding=utf-8
import numpy as np

#索引和切片
a = np.arange(10)
print a[0],a[2],a[-1]
print a[0:5:2]
print a[0::3]
print a[:8:4]
print a[::-1]
print '\n'

a = np.diag(np.arange(3))
print a[1,1]
print a[2,1]
a[2,1] = 10
print a[2,1]
print a[1]
print a[0,:] #行
print a[:,0] #列