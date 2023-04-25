#
#? 文件编码
#* 概念：翻译的规则,如UTF-8,GBK,Gig5等等

#? 文件操作
#* 文件：一篇文章，一段视频等等都可以保存为一个文件
#* 操作：打开，关闭，读，写
#* 打开文件 -> 读写文件 -> 关闭文件

#? 打开文件
#  open(name,mode,encoding)
#  name:是文件名的字符串
#  mode:是打开文件的模式：只读r，写入w，追加a,后两个模式可以创建新文件
#  encoding:编码格式（推荐UTF-8）
f = open('hello.txt','r',encoding="UTF-8")
print(type(f))



#? 读取文件
#  文件对象.read(num)   num表示读取的数据的长度,最后f的指针会停在相应位置
print(f"读取10个字节的结果：{f.read(10)}")
print(f"再读取10个字节的结果：{f.read(10)}")
print(f"剩余的内容是：{f.read()}")
#  文件对象.readlines()  返回值为字符串列表，0为第一行，1为第二行...
f = open('hello.txt','r',encoding="UTF-8")
print(f"内容是：{f.readlines()}")
#  文件对象.readline()  一次读取一行内容，返回一行的字符串
f = open('hello.txt','r',encoding="UTF-8")
print(f"第一行是：{f.readline()}")
print(f"剩余内容是：{f.read()}")

#! 可以使用for来读取每一行
f = open('hello.txt','r',encoding="UTF-8")
for line in f:
    print(f"每一行数据是:{line}")



#? 关闭文件
#  文件对象.close()  
#* with open as 文件变量名:
#*     ......一系列操作
#  会自动关闭文件


#? 文件写入
#  文件对象.write(str)  这时候存到缓冲区中
#? 内容刷新
#  文件对象.flush()  这是为了提高效率，把缓冲区中的内容存到了硬盘中
f = open('hello.txt','w',encoding="UTF-8")
f.write("hello")  # w 模式，如果已有文件，会把原本的内容全都覆盖！
#  f.flush() 
f.close() # close()自带flush方法，可以不写flush()

#? 文件追加
f = open('hello.txt','a',encoding="UTF-8")
# 除了把'w'改为'a'，其他方法相同
f.write(" Hello World!!!!\n")
f.close()



# 综合案例：备份一个文件