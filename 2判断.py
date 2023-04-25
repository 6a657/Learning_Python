# ? bool 类型
# ?True表示真，False表示假
# ?可以表示比较运算符的结果,有 ==  !=  >  <  >= <=
result = 10>5
print(result)
result = 10==5
print(result)
print(type(result))
print(f"10 > 5结果是：{10 > 5}")


# ?if语句的基本格式，通过缩进来配对
"""
  if 要判断的条件:  # !一定要加冒号！
    条件成立时，要做的事情
"""

age = 18
print(f"今年我已经{age}岁了")
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")

# !一定要有4个空格缩进
print("时间过得真快！")



# ?if-else 语句的使用
age = int(input("请输入你的年龄："))
if age >= 18:
    print("你已成年，需要买票10元。")
else:   # !与if同级的else一定与if有相同缩进，而且有冒号
    print("你未成年，可以免费游玩。")# !同理有4个空格缩进


# ?if-elif-else 多条件判断 空格缩进也必须
"""
if 条件1:
    ......
elif 条件2:
    ......
elif 条件3:
    ......
else:
    ......
"""
"""if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费")
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("vip级别大于3，可以免费")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费")
else:
    print("不好意思，条件均不满足，需要买票10元")"""
# 可以在判断中，直接写input，来简洁代码与操作

# ?条件判断的嵌套判断语句
# !空格缩进是极其重要的！
"""if int(input("请输入你的身高（cm）：")) > 120:
    print("身高超出限制，不可以免费！")
    print("但是，如果vip级别大于3，可以免费")
    if int(input("请输入你的VIP等级（1-5）：")) > 3:
        print("恭喜你，vip级别达标，可以免费")
    else:
        print("Sorry 你需要买票10元")
else:
    print("欢迎小朋友，免费游玩")
"""

# ?案例：猜数字
import random
num = random.randint(1,10)  # *产生随机数的方式
find = False
count = 0
while count<3:
    guess = int(input("请猜猜这个数："))
    if(guess>num):
        print("大了")
    elif(guess<num):
        print("小了")
    else:
        print("猜对啦！")
        find = True
        break
    count += 1
if find==False:
    print(f"抱歉，你没猜到，这个数字是{num}")
