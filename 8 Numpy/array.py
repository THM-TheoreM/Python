#encoding=utf-8
import numpy as np

#一维数组
a = np.array([0,1,2,3])
print a,a.ndim,a.shape,len(a)

#二维数组
b = np.array([[0,1,2],[3,4,5]])
print b,b.ndim,b.shape,len(b)

#多维数组
c = np.array([[[1],[2]],[[3],[4]]])
print c,c.ndim,c.shape,len(c)

#等间距分布的数组
d = np.arange(10)
print d
d = np.arange(1,9,2)
print d

#指定长度的数组
e = np.linspace(0,1,6)
print e
e = np.linspace(0,1,5,endpoint=False)
print e