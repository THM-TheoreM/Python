#encoding=utf-8
import numpy as np
import pylab as pl
from scipy.integrate import quad
from scipy import signal

#数值积分：scipy.integrate
res, err = quad(np.sin, 0, np.pi/2)
print np.allclose(res,1)
print np.allclose(err,1-res)

#信号处理：scipy.signal
#移除信号的线性趋势
t = np.linspace(0, 5, 100)
x = t + np.random.normal(size=100)
pl.plot(t, x, linewidth=3)
pl.plot(t, signal.detrend(x), linewidth=3)
pl.show()

#使用FFT重采样n个点
t = np.linspace(0, 5, 100)
x = np.sin(t)
pl.plot(t, x, linewidth=3)
pl.plot(t[::2], signal.resample(x, 50), 'ko')
pl.show()

#图像处理：scipy.ndimage
#1 图像的几何变换
#2 图像滤镜
#3 数学形态学
#4 图像测量