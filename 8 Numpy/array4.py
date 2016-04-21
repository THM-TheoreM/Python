#encoding=utf-8
import numpy as np

#copy and view
a = np.arange(10)
b = a[::2]
print np.may_share_memory(a,b)

b[0] = 12
print b
print a

a = np.arange(10)
b = a[::2].copy()
print np.may_share_memory(a,b)

b[0] = 12
print b
print a

#Fancy indexing
np.random.seed(3)
a = np.random.random_integers(0,20,15)
print a
mask = (a%3 == 0)
print mask
b = a[mask]
print b
print np.may_share_memory(a,b)

a = np.arange(0,100,10)
print a
b = a[[2,3,2,4,2]]
print b
print np.may_share_memory(a,b)