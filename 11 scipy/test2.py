#encoding=utf-8
from scipy import linalg
import numpy as np

#线性代数运算：scipy.linalg
#行列式
arr = np.array([[1,2],[3,4]])
print linalg.det(arr)

#逆
arr = np.array([[1,2],[3,4]])
iarr = linalg.inv(arr)
print iarr

#svd分解
arr = np.arange(9).reshape((3,3))+np.diag([1,0,1])
uarr, spec, vharr = linalg.svd(arr)
print spec

sarr = np.diag(spec)
svd_mat = uarr.dot(sarr).dot(vharr)
print svd_mat

#快速傅里叶变换：scipy.fftpack