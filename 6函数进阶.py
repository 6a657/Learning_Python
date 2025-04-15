#
#?  函数的多个返回值:用逗号隔开即可
def test_return():
    return 1,2,3
x,y,z = test_return()
print(x,y,z)

#? 函数参数种类
# 1.位置参数，调用函数时按照函数定义的参数位置来传递参数
# 2.关键字参数，函数调用时通过 键值对 传递参数
def user_info(name,age,gender):
    print(f"你的名字是：{name}，年龄是：{age}，性别是：{gender}")
user_info(name="小明",gender="男",age=20)
user_info("小明",age=20,gender="男")  #可以与位置参数混用，但位置参数一定在关键字参数前面
# 3.缺省参数，也称为默认参数
# def user_info(name,age,gender="男")，可以被覆盖，但是必须在最后的参数设置 
# 4.不定长参数
#        位置不定长：返回元组
def user_inffo(*args): #! 一个星号
    print(args)
user_inffo('hello',25)
#        关键字传递：返回字典
def user_infffo(**kwargs):  #! 二个星号
    print(kwargs)
user_infffo(name='小王',age=11) 


#? 函数传参：即使用一个函数作为另一个函数的参数
def test_func(compute,x,y):
    result = compute(x,y)
    print(result)
def compute(x,y):
    return x+y
test_func(compute,1,2)
#! 代码的执行逻辑的传递,即传入函数指针


#? 匿名函数
#  函数的定义中：
#  def关键字，可以定义带有名称的函数
#  lambda关键字，可以定义匿名函数，但只可临时使用一次
def test(compute):
    result = compute(1,2)
    print(result)
test(lambda x,y:x+y)  #仅在此次调用中使用
#!  lambda 传入参数: 函数体(只能一行代码)