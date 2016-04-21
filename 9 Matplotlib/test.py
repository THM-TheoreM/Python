#encoding=utf-8
from matplotlib import pyplot as plt
import numpy as np

#plot
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
c,s = np.cos(x),np.sin(x)
plt.plot(x,c)
plt.plot(x,s)
plt.show()

#1.4.2.2-1.4.2.10