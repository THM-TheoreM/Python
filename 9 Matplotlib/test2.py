#encoding=utf-8
from matplotlib import pyplot as plt
import numpy as np

#subplot
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s = np.cos(x),np.sin(x)

plt.figure(1) #创建图表1
plt.plot(x,c)

plt.figure(2) #创建图表2
plt.subplot(211) #创建子图1
plt.plot(x,c)
plt.subplot(212) #创建子图2
plt.plot(x,s)

plt.show()

#1.4.4-1.4.6