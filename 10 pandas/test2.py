#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

#缺失值处理
df1 = df.reindex(index=dates[0:4],columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
print df1

df1.dropna(how='any')
print df1

df1.fillna(value=5)
print df1

pd.isnull(df1)
print df1

#相关操作
#1 统计
#2 apply
#3 直方图
#4 字符串方法

#合并
#1 concat
#2 join
#3 append

#分组
#1 splitting
#2 applying
#3 combining

#reshaping
#1 stack
#2 数据透视表