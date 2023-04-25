#
#? 函数：是组织好的，可重复使用的，实现特定功能的代码段

#? 函数的定义语法：
# def 函数名(传入参数):
#     函数体
#     return 返回值
def length(name):
    count =0
    for x in name:
        count += 1
    return count     #? 等效于len()函数
na = "djafjjibgae"
print(f"{length(na)}")
print(f"{len(na)}")

#! 参数与返回值都不是必须的，可以省略
#! 函数必须先定义后使用
#! 可以使用很多个参数，而且不需要声明类型

#? 函数返回值的定义，与c语言相同，略
#? None类型，是函数无返回值是的返回值，即任何一个函数都会有返回值
def ss():
    print("hahaha")
result = ss()
print(f"无返回值函数，返回的内容是:{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

#* None 有什么用呢？
#* None 在if判断上 等效于 False
def check_age(age):
    if age>18:
        return "SUCCESS"
    return None
result = check_age(5)
if not result:
    print("未成年，不可进入")
#* 也可用于声明无内容的变量上,如果暂时不需要变量有具体值
name = None


#? 函数的说明文档，即加注释
# def func(x,y):
#     """
#     函数说明
#     ......
#     """
#     函数体
#     return 返回值
def add(x,y):
    """
    add函数可以接受2个参数，进行2数相加的功能
    x:表示相加的其中一个数字
    y:表示相加的另一个数字
    return: 返回值是2数相加的结果
    """
    result = x + y
    print(f"2数相加的结果是：{result}")
    return result

add(5,6)  #? 鼠标悬停可以查看函数的说明文档


#? 函数的嵌条调用，即一个函数里面又调用了另外一个函数，略

#? 函数的变量作用域
#? 变量作用域，分为局部变量与全局变量
# 局部变量
def test_a():
    num = 100
    print(num)
test_a()
#! print(num) 不可以访问

# 全局变量
nu = 200
def test_b():
    nu = 500   #! 如果没有这句话，会显示200，但局部变量的优先级更大
    print(f"test_b{nu}") #! 这意味着函数改不了全局变量（目前为止）
test_b()
print(f"{nu}")

#? 但是如果要在函数内修改全局变量，该怎么办？
#* 使用global 关键字
n = 200
def test_c():
    global n
    n = 500
    print(f"test_c {n}")
test_c()
print(n)