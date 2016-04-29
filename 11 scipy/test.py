#encoding=utf-8
from scipy import io as spio
import numpy as np

#文件输入/输出：scipy.io
#导入和保存matlab文件
a = np.ones((3,3))
spio.savemat('file.mat',{'a':a})
data = spio.loadmat('file.mat',struct_as_record = True)
print data['a']

#读取图片
#imread: http://stackoverflow.com/questions/15345790/scipy-misc-module-has-no-attribute-imread

#特殊函数：scipy.special