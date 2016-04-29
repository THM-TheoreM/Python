#encoding=utf-8
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

#优化和拟合：scipy.optimize
#找到标量函数的最小值
def f(x):
	return x**2 + 10*np.sin(x)

x = np.arange(-10,10,0.1)
#plt.plot(x,f(x))
#plt.show()	

print optimize.fmin_bfgs(f,0) #BFGS算法
print optimize.fmin_bfgs(f,3,disp=0)
print optimize.brute(f,((-10,10,0.1),))
print optimize.fminbound(f,0,10)

#找标量函数的根
root = optimize.fsolve(f,1)
print root
root = optimize.fsolve(f,-2.5)
print root

#曲线拟合
xdata = np.linspace(-10,10,num=20)
ydata = f(xdata) + np.random.randn(xdata.size)

def f2(x,a,b):
	return a*x**2 + b*np.sin(x)

guess = [2,2]
params, params_covariance = optimize.curve_fit(f2,xdata,ydata,guess)
print params

#统计和随机数：scipy.stats
#1 直方图和概率密度函数
#2 百分位
#3 统计检测

#插值：scipy.interpolate