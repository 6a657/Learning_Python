
# * while的基础使用
"""
while 条件:
    ......
    ......
    
"""
#? 只要条件满足，会无限循环进行
i = 0
Sum = 0
while i<100:  #! 条件必须是bool型
    Sum += i  #! 要加冒号，要保证缩进
    i += 1    #! 不能无限循环
print(Sum)

#? while循环嵌套，与判断语句嵌套相同，不管
# 打印99乘法表
# print输出不换行方法：print("..." , end='')
print("hello",end='')
print("world",end='')
# 字符串对齐：使用\t来对齐,这是制表符
print("Hello World")
print("itheima best")
print("Hello\tWorld")
print("itheima\tbest")

i=1
j=1
while i<10:
    while j<=i:
        print(f"{i}*{j}={i*j}\t",end='')
        j += 1
    print('\n')
    i += 1
    j = 1


#? for循环的基础语法
# for循环是一种“轮询”机制，是对一批内容进行分别处理,直到结束,称为遍历循环
# for 临时变量 in 待处理数据集:
#     ......
name = "itheima is a brand of itcast"
count = 0
for x in name:
    if(x=='a'):
        count += 1
print(f"被统计的字符串中有{count}个a")
#! 把字符串中的一个个字符取出来处理，直到没有为止
#! 无法定义循环条件，理论上，无法构建无限循环，也要有空格缩进

#? range语句
#? for中的待处理数据集，称之为序列类型，指其内容可以一个个依次取出的一种类型
#? 包括 字符串 列表 元组 等
#? range函数可以获得序列，以数字序列为例
# 1.range(num) 获得从0开始，到num结束的数字序列（不包含num）
# 如range(5) 获得的数据为: [0,1.2.3.4]
for x in range(10):
    print(x,end=" ")
print("\n")
# 2.range(num1,num2) 同理，不包含num2
for x in range(5,10):
    print(x,end=" ")
print("\n")
# 3.range(num1,num2,step) 同理，不包含num2，但步长为step
for x in range(5,10,2):
    print(x,end=" ")
print("\n")


#? 变量作用域
# for x in range(10):
#     print(x)
# print(x)
#! 编程规范上，原则上外部是不可以访问到x中的，但实际上是可以的，但不建议
#! 不过可以通过提前定义来解决这个困扰

#? for循环的嵌套运用：重点：空格缩进，变量作用域，其余同if嵌套

#? continue 与 break 的使用，用于跳出循环与跳出单步循环
#? continue/break
# for i in range(1,100)
#     ......
#     continue
#     ......   #则该语句不会进行，常常与if判断连用