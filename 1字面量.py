print("hello world!")
print(666)
print(13.14)
print("叶子")

# 注释
# 单行注释：以"#"为开头
"""
  多行注释：以3个“开头，以3个”结尾
"""


# 定义变量，记录钱包余额
money = 50
print("钱包还有：",money)
money = money - 10
print("买了冰淇淋花了10元，还剩下",money,"元")
# 假设，每隔一小时输出钱包余额
print("现在是下午1点，钱包余额剩余：",money)


# 数据类型
print(type(666))
print(type(1.1))
print(type("叶子"))
a = type(666)
print(a)
print(type(a))
name = "叶子"
name_type = type(name)
print(name_type)


# 数据转换类型，实际应用很多
# int() float() str()
num_str = str(111)
print(num_str)
print(type(num_str))
float_str = str(11.232)
print(type(float_str),float_str)
#将字符串转换成数字
num = int(11.73)
print(type(num),num)
"""
num1 = int("叶子")
print(type(num1),num1)
"""
num2 = float("-9.3404")
print(type(num2),num2)


# 标识符
# ?合法 hello _009 A_9da9 _9 true Class
# !非法 989 sg*jf _A--3 False def
# 变量的命名规范
# 1.见名知意  2.下划线命名法 


# 运算符
# ? + - * / // % **
print(6//4)
print(6%4)
print(6**4)
# 赋值运算符 = 
# ? +=  -=  *=  /=  %=  **=  //=


# 字符串扩展内容
# 字符串定义方式
name = '叶子'
name = "叶子"
name = """叶子""" #三引号定义法，与注释一样，如果没有变量接受它，就变成注释了
# 字符串内如果有引号呢？
"""
   单引号定义法，可以内含双引号，反之亦然
   也可以使用转义字符 \ 来接触引号的效用，变为普通字符串
"""
print('"你好！我是叶子"')
print("我说：'你很好！'")
print("我说一遍：\"我才好\"")
# 字符串的拼接 用+进行拼接
print("叶子" + "是绿色的")
name = "叶子"
address = "中国"
tel = 40039420021
print(name + address ) #字符串无法用加号与数字等其他类型进行拼接
# 怎么办？
# 字符串格式化,使用%s占位符实现字符串的替换
print("你好%s"%name)
print("%s   %s"%(name,address),tel)
# 通过占位的形式，完成数字与字符串的拼接
class_num = 57
salary = 12222
message = "来吧！北京%d,工资%s" % (class_num,salary)
print(message)#其中将数字隐式转换为字符串，如果还是想以原本的形式，可以用%d %f等

# 格式化的精度控制  %5.6f,但会进行四舍五入,如果宽度小于数字长度，则宽度限制无效
print("%5.2f"%(5.6754))
# 快速格式化  用f开头来提示，然后里面用{}语法就可以了，但不理会类型，不做精度控制
print(f"我是{name},年龄{class_num},月薪{salary}")
# 对表达式进行格式化，其实本质是用返回值格式化来使用的
#表达式：一条具有明确执行结果的代码语句，如1+1 5*2 name="叶子"

#综合练习

name = "公司名"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价{stock_price}")
print("每日增长系数是：%s，经过%d的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*(stock_price_daily_growth_factor**growth_days)))

#数据输入：键盘输入,不管你写的是什么，都会以字符串类型传出去
name = input("请告诉我你是谁？")
print("我知道了，你是%s"%name)
age = input("请输入你的年龄")
age = int(age)
print("age类型是%s"%type(age))