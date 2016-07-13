# Python

## 安装

- [官网](https://www.python.org)下载
 
- 将python的安装目录添加到环境变量的path中（若在安装时勾选add path，可以免去这个步骤）

## 编辑器

- 自带编辑器

  - IDLE（Pyhon GUI）：支持脚本式

  - Python（command line）：支持交互式
 
- Notepad++

  - PyNpp：支持交互式和脚本式
 
  - Python Script：支持交互式

  - NppExec：支持脚本式
 
- Sublime3
 
  - 使用插件前需先安装package control

  - SublimeREPL可使得sublime上运行各类语言，如NodeJS，python，ruby，scala和haskell等等
  
- Anaconda
 
   - [官网](https://www.continuum.io/downloads)下载

   - 安装简单，集成各类科学计算库，无需再下载python

## 编译

- [python的编译机制]http://www.open-open.com/lib/view/open1380418623307.html

## 模块

- 安装

  - [python模块常用的几种安装方式](http://blog.163.com/yang_jianli/blog/static/161990006201162152724339)

  - 下载exe安装，比如[scipy](http://download.csdn.net/detail/caanyee/8241305)

```
  pip freeze：查看所有模块
   
  pip list --outdated：查看所有过期模块

  pip install --upgrade xxxx：升级xxxx模块
```

  - 更新提示`You are using pip version 8.1.1，however version 8.1.2 is available`导致不能使用pip命令，可使用命令`easy_install.exe pip==8.1.2`

- 导入

```
  import module：使用模块，需要加类名加以访问和调用

  import module as xxxx：把模块当做xxxx使用
 
  from module import *：使用模块，可直接访问和调用其中的类
 
  from module import xxxx：使用模块，可直接访问和调用指定的类xxxx
```

## 教程
 
- [菜鸟教程](http://www.runoob.com/python/python-tutorial.html)
 
- [廖雪峰的python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

- [The Hitchhiker's Guide to Python!](http://docs.python-guide.org/en/latest)

## 参考书目

- [python核心编程](https://www.gitbook.com/book/wizardforcel/core-python-2e/details)
 
- [笨办法学python](https://www.gitbook.com/book/wizardforcel/lpthw/details)

- [learn python the hard way](http://learnpythonthehardway.org/book/preface.html)

