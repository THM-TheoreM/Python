#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#创建对象
s = pd.Series([1,3,5,np.nan,6,8])
print s
print s.dtypes

dates = pd.date_range('20130101',periods=6)
print dates

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print df
print df.dtypes

df2 = pd.DataFrame({'A':1.,
                    'B': pd.Timestamp('20130102'),
					'C': pd.Series(1, index=list(range(4)), dtype='float32'),
					'D': np.array([3]*4, dtype='int32'),
					'E': pd.Categorical(['test','train','test','train']),
					'F': 'foo'}) 
print df2
print df2.dtypes
print '\n\n\n'

#查看数据
print df.head()
print df.head(3)
print df.tail(4)
print df.index
print df.columns
print df.values
print df.describe()
print df.T
print df.sort_index(axis=1, ascending=False)
print df.sort(columns='B')

#选择
#获取
#通过标签选择
#通过位置选择
#布尔索引
#设置