#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#画图

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(1000,4), index=ts.index, columns=['A','B','C','D'])
df = df.cumsum()
df.plot()
plt.show()

#导入和保存数据
#1 csv
#2 hdf5
#3 excel