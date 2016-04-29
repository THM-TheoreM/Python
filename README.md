# Python

**安装Python**

 - 下载Python
  
   - https://www.python.org/
 
 - 安装Python
 
   - 在环境变量中的path加上安装路径（例如：D:\Program Files\Python27）
   
   - 在安装时勾选add path可以免去这个步骤
 
 - 如果python上各类库的安装不顺利，可以直接下载Anaconda版Python.(安装简单，集成各类科学计算库，无需再下载python)
 
   - https://www.continuum.io/downloads

**编辑Python**

 - Python有自带的编辑器IDLE(Pyhon GUI)，Python(command line)
 
 - 使用notepad++

   - PyNpp：支持交互式和脚本式编程
 
   - Python Script：支持交互式编程
 
 - 使用sublime3
 
   - 使用插件前需要先安装 Package Control

 - 推荐插件
  
    - Anaconda：各类高级功能
  
    - SublimeREPL：使得sublime上运行各类语言（NodeJS，Python，Ruby，Scala 和 Haskell 等等）

**Python的编译器和解释器**

 - http://www.open-open.com/lib/view/open1380418623307.html

 - ipython是一个python的交互式shell，比默认的python shell好用得多

**安装Python模块**

 -  http://blog.163.com/yang_jianli/blog/static/161990006201162152724339/

 - 下载exe文件，比如http://download.csdn.net/detail/caanyee/8241305

**学习Python**
 
 - http://www.runoob.com/
 
 - http://www.liaoxuefeng.com/

 - http://docs.python-guide.org/en/latest/

**模块module**

模块包含了

 - 类
 
 - 变量

 - 函数
 
模块的导入，目的是访问和调用函数或者类

 - import module：访问和调用全部函数和类，需要加模块名
 
 - from module import *：访问和调用全部函数和类，不用加模块名
 
 - from module import foo：访问和调用指定函数和类，不用加模块名

 - import module as a：把a当做module使用

**类class**

类包含了

 - 属性（属性成员，数据成员）和方法

   - 属性分为类变量和实例变量
  
   - 成员分为公有成员和私有成员（通过foo和\__foo区别，还要注意\_foo，\__foo\__的用法）
 
 - 方法重写
 
 - 方法重载 

**变量variable**

 - string

 - list
 
 - tuple
 
 - dict
 
 - set
 
**生成器generator&迭代器iterator**

 - 上面的variable不是迭代器，不是惰性序列
 
 - 生成器是迭代器，是惰性序列 

**函数式编程functional programming**

 - 高阶函数：参数为函数
 
 - 返回函数：return的值为函数
 
 - 装饰器：高阶函数+返回函数
 
 - 匿名函数：lambda创建没有名字的函数

**MySQL**

 - http://www.runoob.com/python/python-mysql.html
 
**numPy**

 - 操作矩阵，类比matlab的部分功能

 - http://scipy-lectures.cn/intro/numpy/index.html

**matplotlib**

 - 绘制图表，类比matlab的部分功能

 - http://scipy-lectures.cn/intro/matplotlib/matplotlib.html

**pandas**

 - 存放，索引数据，类比SQL

 - http://www.cnblogs.com/chaosimple/p/4153083.html

**scipy**

 - http://blog.csdn.net/lwfcgz/article/details/23290623

**scikit-learn**