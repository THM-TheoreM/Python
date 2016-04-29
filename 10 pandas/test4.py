#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#categotical
df = pd.DataFrame({'id':{1,2,3,4,5,6}, 'raw_grade':['a','b','b','a','a','e']})
df['grade'] = df['raw_grade'].astype('category')
print df['grade']

df['grade'].cat.categories = ['very good', 'good', 'very bad']
df['grade'] = df['grade'].cat.set_categories(['very', 'bad', 'medium', 'good', 'very good'])
print df['grade']

print df.sort('grade')

print df.groupby('grade').size()