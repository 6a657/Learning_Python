#
#? 数据容器，即可以容纳多份数据的 数据类型，每一份数据称为1个元素
#? 每一个元素，可以说任意类型的数据，如字符串，数字，布尔等

#* 根据特点不同，分类数据容器
#  1.是否支持重复元素
#  2.是否可以修改
#  3.是否有序
#* 分为五类，分别是
#? 列表list，元组tuple，字符串str，集合set，字典dict



#*################################################################
#*################################################################
#? 列表list
# 字面量
#* [元素1, 元素2, 元素3, 元素4, 元素5, ...]

#定义变量
#* 变量名称 = [元素1, 元素2, 元素3, 元素4, 元素5, ...]
name_list = ['Beijing','Tianjin','Nanning']
print(name_list)
print(type(name_list))

my_list = ['Nanning',666,True]
print(my_list)           #? 列表中的元素类型可以是不同的
print(type(my_list))     #? 这意味着2维列表是可以实现的

# 嵌套列表
my_list = [[1,2,3],[4,5,6]]


#? 列表的下标索引，与数组的相同，从0开始
print(name_list[1])  #正向索引  0 1 2 3 4...
print(name_list[-1]) #反向索引  -1 -2 -3 -4...

# 嵌套列表的取出
print(my_list[0][-1])


#? 列表的常用操作
# 插入  删除  清空  修改  统计元素个数

#? 列表的查询功能(方法)
# 方法定义：python 中，如果把函数定义为class的成员，那么称函数为方法
#  class Student:
#      def add(self,x,y)
#          return x+y
#  即称add()为Student类的一个方法
#  函数的使用: num = add(1,2)
#  方法的使用: student = Student()
#             num = student.add(1,2)

#? 查询某一个元素
#  list.index(元素)，会返回对应的下标索引
mylist = ['a','b','c']
index = mylist.index('b')
print(f"b在列表中的下标索引值是：{index}")
#  如果不存在，程序会报错
"""
index = mylist.index('d')
print(f"b在列表中的下标索引值是：{index}")
"""

#? 修改list中某位置的值
#  list[index] = value 即可修改
mylist[0] = 'd'
print(mylist)
mylist[0] = 'a'

#? 向list中在指定的位置插入指定元素
#  list.insert(index,object)
mylist.insert(1,'z')
print(mylist)

#? 向list中追加指定元素到列表的尾部
#  list.append(object)
mylist.append('y')
print(mylist)

#? 向list中追加另一个list
#  list.extend(other list)
mmylist = [1,2,3,4,5]
mylist.extend(mmylist)
print(mylist)


#? 删除list中的某个元素

#*--- 指定list下标进行删除 ---
#  1. del list[index]  仅仅实现删除
del mylist[1]
print(mylist)
#  2. list.pop(index) 返回值为删除的元素
element = mylist.pop(0) #! 也可以反向索引方法
print(f"取出元素为{element}，列表变为{mylist}")

#*--- 指定list内容进行删除 ---
#  list.remove(object)  从前到后搜索
mylist.remove(1)
print(mylist)


#? 清空列表
#  list.clear()
mylist.clear()
print(mylist)
mylist = ['a','b','c','a']

#? 统计列表中某元素的数量
#  list.count(object)
print(f"a元素的数量为{mylist.count('a')}")

#? 获得列表的全部元素数量
#  len(list)
print(f"列表的长度为{len(mylist)}")


#*  终上所述，方法共有11个，分别为
#*  list.append(object) list.extend(list) list.insert(index,object)  del list
#*  list.pop(index) list.remove(object) list.clear() list.count(object)
#*  list.index(object) len(list)  list[index]


#* list的特点：
#  1.可容纳多个元素   2.数据是有序储存的   3.允许重复数据存在  4.可以修改

#* list的遍历操作：
# index = 0    while循环
# while index < len(list):
#     object = list[index]
#     some methods to object
#     index += 1
#
# for x in list:  for循环
#     some methods to x

kk = [1,2,3,4,5,6,7,8,9,10]
k = []
for x in kk:
    if(x%2==0):      #取出偶数的操作
        k.append(x)
print(k)

#*################################################################
#*################################################################
#? 元组tuple

#  元组字面量
#* (元素，元素，...)
#  定义元组变量
#* 变量名称 = (元素，元素，...)
#* 定义单个元素的元组： 
t = ("hello",) #! 必须带逗号，不然直接变成object了而不是tuple
print(t)
#  定义空元组
#* 变量名称 = ()
#* 变量名称 = tuple()

#! 除了元组不可修改外，其他方面与list相同
#* 方法共有4个
#* tuple.index(object)  tuple.count(object)  len(tuple)  tuple[index]

#! 但是如果元组内部为list，这list可以修改
t = (1,2,[1,2,3])
print(f"t的内容是{t}")
t[2][1] = 55
print(f"t的内容是{t}")

#* list的特点：
#  1.可容纳多个元素   2.数据是有序储存的   3.允许重复数据存在  4.不可以修改
#  5.但是内部的list支持修改


#*################################################################
#*################################################################
#? 字符串string
# 它是数据容器，可以视为只有字符的list
my_str = "China"
value = my_str[2]
value2 = my_str[-1]
print(f"value的值为{value},value2的值为{value2}")


#? 在str中查找字符串
#  str.index(find_str) 返回第一个下标

#? 字符串的替换
#  str.replace(str1,str2)
#! 将str中的所有str1换为str2，返回值为新的字符串，但原本的str是不变的

#? 字符串的分割
#  str.split(char)
my_str1 = "China France English"
my_str1_list = my_str1.split(" ")
print(f"将字符串{my_str1}进行split切分后得到:{my_str1_list},类型是:{type(my_str1_list)}")

#? 字符串的规整操作
#  str.strip("char1char2...")  #! 要有引号，要传入字符串！
my_str1 = "   114514   "
print(my_str1.strip())   # 去除前后空格
my_str1 = "112214323452322112"
print(my_str1.strip("12"))  # 去除前后所有的 1 和 2
#! 用于去除字符串前后的对应字符

#? 字符串的计数方法
#  str.count(str1)  len(str)

#* 方法共有7个
#* str.index(str1)  str.replace(str1,str2)  str.split(str1)
#* str.strip(str1)  str.count(str1)  len(str)  str[index]

#* 遍历方法与list相同

#* string的特点：
#  1.只可以存储字符串  2.不可以修改  3.支持下标索引  4.允许重复字符串存在

#? eg:
str = "itheima itcast boxuegu"
str_it_count = str.count("it")
str_change = str.replace(" ","|")
str_device = str_change.split("|")
print(str_device)
print(str_change)



#*################################################################
#*################################################################
#? 数据容器的切片操作
#? 序列定义：
#* 内容有序，连续，可使用下标索引的一类数据容器
#* 列表，元组，字符串均可以视为序列

#? 切片操作：
#* 从一个序列中，取出一个子序列
#  语法： 序列[beginning:ending:steps]
#! 若步长为负数，表示反向取，而beginning与ending都要反向标记
#! 而此操作不会改变原始序列，step为1，可省略不写
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]
print(result1)
# [1,2,3] 最后一个不计入结果中
result2 = my_list[0:7:2]
print(result2)
# [0,2,4,6]
result3 = my_list[::-1]
print(result3)
# [6,5,4,3,2,1,0]
result4 = my_list[::-2]
print(result4)
# [6,4,2,0]
result5 = my_list[:-2]
print(result5)



#*################################################################
#*################################################################
#? 集合set
# 好处：可自带查重功能

#  集合字面量
#*  {number1,number2,...}
#  定义集合变量/空集合
#  my_set = set() 而不可以用 my_set = {}，这个定义方式被字典占用了
my_set = {'a','b','b','c','d','e','f'}
print(my_set)
#! 显然，集合是不重复的，无序的，故不支持下标索引访问
#! 但是set与list是一样的，是允许修改的

#*  集合操作
#?  添加新元素
#   set.add(object)
my_set.add('g')
my_set.add('a')
print(my_set)  #已有的元素是进不去的

#? 移除元素
#  set.remove(object)

#? 随机取出一个元素
#  set.pop()
#  且集合也被改变

#? 清空集合
#  set.clear()

#? 取出2个集合的差集
#  set2.difference(set2)
set1 = {1,2,3,5}
set2 = {2,4,5,6}
print(f"{set1.difference(set2)}")

#? 消除2个集合的差集
#  set1.difference_update(set2)
#  即删除集合1内与集合2相同的元素
set1.difference_update(set2)
print(f"{set1}")

#? 取2个集合的并集
#  set1.union(set2)
print(f"{set1.union(set2)}")

#? len(set)  略
set1 = {1,2,2,2,3,4,4,5,5,6,7,7,7,7,7,7}
print(f"{len(set1)}")
# 7

#? 集合的遍历
#! 由于集合不支持下标索引，故不可用while循环，但可以用for循环遍历

#* set的特点：
#  1.可以容纳多个数据  2.可以容纳不同类型  3.数据是无序存储的
#  4.不允许重复数据存在   5.可以修改   6.支持for循环

#* set的操作
#* set.add(object)  set.remove(object)  set.pop()  set.clear()
#* set1.difference(set2)  set1.difference_update(set2)
#* set1.union(set2)  len(set)




#*################################################################
#*################################################################
#? 字典dict

#* 字典的定义：[字]:[含义]  /  key:value
#  {
#    "aaa":34,
#    "vvv":55,
#    "dddd":4283
#  } #可以通过key来获取value
#* 定义字典字面量
{ "aa":32, "d2":42, "ff8a":24}
#* 定义空字典
#  my_dict = {} / my_dict = dict()
#! 字典与集合是相同的！不允许key的重复！如果重复也会去重
#! 字典与集合一样，不可用下标索引，但可以用key得到相应的value
#  dict[key] = value
my_dict = {"yy":55,"aa":64,"bb":89}
score = my_dict['yy']
print(score)

#! 字典的key与value可以是任意数据类型（但key不可以为字典）
#! 这说明，字典是可以嵌套的
# {
#   "姓名":{
#     "语文":65,
#     "数学":77,
#     "英语":44
#   },
#   "姓名":{
#     ......
#   }
# }


#* 字典的常用操作

#? 新增元素/更新元素
#  dict[key] = value
my_dict["cc"] = 99
print(my_dict)
#! 由于字典key不可重复，所以如果key是dict已有的，则会修改对应的value值

#?删除元素
#  dict.pop(key)
#* 会获得key对应的value，且删除对应的key:value

#?清空字典
#  dict.clear()

#? 获得字典的所有key
#  dict.keys()
keys =  my_dict.keys()
print(keys)  # 以list的形式存在

#? 遍历字典
#* 既然可获得所有key，自然可以以for进行遍历
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")

#* 也可以直接用for进行遍历，每一次循环是直接得到key
for key in my_dict:
    print(f"字典的key是{key}")
    print(f"字典的value是{my_dict[key]}")

#! 而while遍历是不行的

#? len(dict) 略

#*  dict操作
#*  dict[key]  dict[key]=value  dict.pop(key)
#*  dict.clear()  dict.keys()  len(dict)

#*  dict特点
#  1.可容纳多个数据   2.可容纳不同类型的数据   3.不支持下标索引
#  4.可以修改  5.支持for，不支持while  6.每一份数据为key:value键值对
#  7.可以通过key获取到value，key不可重复




#*################################################################
#*################################################################
#? 数据容器对比总结：
# 元素类型  下标索引  重复元素  可修改性  数据有序  使用场景
# list  tuple   string   set   dictionary
#? 通用操作
#  for遍历  len()  max()  min()  /字典是比较key谁大谁小，返回key
#? 类型转换
#  list()  tuple()  set()  str()
#! set被转化后 只保留 key（除了str）
#! str() 转化其他容器会保留外面的大括号与里面的分隔的逗号，dict会原封不动的转化
#? 容器的排序
#  sorted(容器)  返回值为从小到大的列表（dict同样只比较key大小）
#  反向排序： sorted(容器,reverse = True)