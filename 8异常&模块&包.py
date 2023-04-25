
#? 异常/BUG 报错
# f = open('fff.txt','r')
#! FileNotFoundError: [Errno 2] No such file or directory: 'fff.txt'
# 1 / 0
#! ZeroDivisionError: division by zero
# print(name)
#! NameError: name 'name' is not defined


#? 捕获异常，对可能出现的bug进行处理
#* 如果出现bug，接下来有2种情况：
#* 1.整个程序因为bug停止运行
#* 2.对bug进行提醒，整个程序继续运行
#? 如果想实现2，就需要用到捕获异常
#? 其作用是：提前假设某处会出现异常，做好提前准备，真的有异常发生时，可以有后续手段
#语法格式：
#try:
#    可能发生错误的代码
#except:
#    如果出现异常执行的代码
try:
    f = open('fff.txt','r')
except:
    print("出现异常了")


#? 捕获指定异常
try:
    print(name)
    # 1/0
except NameError as e:
    print(e , 33)  # e为错误信息，33为当前行数
    print("出现了变量未定义的异常")


#? 捕获多个异常
try:
    print(1/0)
except(NameError,ZeroDivisionError):
    print('ZeroDivision错误...')

#? 捕获所有异常
try:
    print(1/1)
except Exception as e:
    print("出现异常了")
else:
    print("没有异常")
finally:
    print("我是finally,我一定会执行")

#? 总的捕获异常的语法格式
"""
try:
    可能要发生异常的语句
except[异常 as 别名]:
    出现异常的准备手段
[else:]
     未出现异常时要做的时期
[finally:]
     一定会做的事情
"""


#? 异常的传递性，意味着不需要到底层去找错误
# func1发生异常时，func2也会报错，func3也会报错...
def func1():
    print("func1开始执行")
    num = 1/0   #出现错误的位置
    print("func1结束运行")
def func2():
    print("func2开始执行")
    func1()
    print("func2结束运行")
def func3():
    print("func3开始执行")
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常的信息是：{e}")
    print("func3结束运行")
func3()



#?  python 模块(Module)
#?  模块 ：就是一个Python文件，以py结尾
#?  导入语法
#  [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
#  常见的组合形式如：
#  import 模块名1,模块名2...
#  import 模块名 as 别名
#  from 模块名 import 类/变量/方法 等
#  from 模块名 import *
#  from 模块名 import 功能名 as 别名

import time    #导入python内置的time模块
print("你好")
time.sleep(2)  #通过.  就可以使用模块内部的全部功能（类，函数，变量）
print("我好")

from time import sleep
print("222")
sleep(1)
print("444")

from time import *
print(123421)
sleep(1)
print(45642543)

import time as t
print(7645342356)
t.sleep(1)
print(764354243524)


#? 自定义模块
import mokuai
mokuai.test(1,6)
from mokuai import test
test(1,5)

# __name__ 变量可以保证 不会输出产生的结果的
# __all__ 变量可以限定import * 导入的函数数量



#? Python包 但Python的模块太多了 很乱！
#  Python包 就是一个文件夹，在其中包含了一个__init__.py 文件，该文件夹可用于包含多个模块文件
#  从逻辑上看，包的本质依然是模块
#  --------------------------------------
#  - module1  module2                   -
#  - module3  module4  => __init__.py   -  => Package包
#  - module5  module6                   -
#  --------------------------------------

#? 创建包
#  创建文件夹 -> 创建__init__.py 文件 ,可以是空的 ->往里面加入模块
from my_package import mokuai
mokuai.test(5,6)
import my_package.mokuai
my_package.mokuai.test(76,5)


#? 安装第三方包 是第三方开发的 不是官方的
#  使用pip来安装即可 国内： pip install -i https://pypi.tuna.tsinghua.edu.dn/simple 包名称
#  或直接用 pip install 包名称（国外网站）