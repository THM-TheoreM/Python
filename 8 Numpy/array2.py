#encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt

#数据类型
a = np.array([1,2,3])
print a.dtype
a = np.array([1.,2.,3.])
print a.dtype
a = np.array([1,2,3],dtype=float)
print a.dtype
a = np.ones((3,3))
print a.dtype
a = np.array([1+2j,3+4j,5+6*1j])
print a.dtype
a = np.array([True,False,False,True])
print a.dtype
a = np.array(['Bonjour','Hello','Hallo'])
print a.dtype

#可视化
x = np.linspace(0,3,20)
y = np.linspace(0,9,20)
plt.plot(x,y)
plt.plot(x,y,'o')
plt.show()

image = np.random.rand(30,30)
plt.imshow(image,cmap=plt.cm.hot)
plt.colorbar()
plt.show()
