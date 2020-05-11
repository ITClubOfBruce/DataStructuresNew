'''
    哪些问题适合用递归解决
    怎么用递归的方式写程序
    ***** 递归的三大法则
    递归也是一种迭代

    什么是递归？

    一、递归的定义
        递归是一种解决问题的方法，它把一个问题分解为越来越小的子问题,直到问题的规模
        小到可以被很简单直接解决。
        通常为了达到分解问题的效果，递归过程中要引入一个***调用自身的函数***


        [1,2] [3,3]  [6,4] 


    计算 [1,2,3,4,5,6,7] 的和
    
    迭代求和

    def list_sum(my_list):
     the_sum = 0
     for num in my_list:
         the_sum = the_sum + num
     return the_sum

    print(list_sum([1,2,3,4,5,6,7]))


    不能使用循环，计算和   -------->   递归
    （（（1+2）+3）+4）

    列表中的第一个元素和剩余所有的元素列表的和之和
    listSum(numList) = first(numList) + listSum(rest[numList])
    转换成Python
    num_list[0] + num_list[1:] 
    # 递归函数
    def list_sum(num_list):
        # 函数结束运行的必要条件，否则就是一个死循环
        if len(num_list) == 1:
            return num_list[0]
        else:
            return num_list[0] + list_sum(num_list[1:]) 

    print(list_sum([1,2,3,4,5,6,7]))


    二、递归的三大定律
        1. 递归算法必须有个基本结束条件（长度为1的列表）
        2. 递归算法必须改变自己的状态并向基本结束条件演进
        3. 递归算法必须递归地调用自身（核心）


    三、练习
        1. 用list_sum 计算数列[2,4,6,8,10] 要进行多少次递归调用？
        2+sum(4,6,8,10)
        4+sum(6,8,10)
        6+sum(8,10)
        8+sum(10)

        2. 计算某个数的阶乘的递归算法，（最合适的基本结束条件）,假设0！= 1 
        5！= 5*4*3*2*1
        n == 1

        def fact(n):
            if n == 1 or n == 0:
                return 1
            else:
                return n*fact(n-1)

        print(fact(5))



    四、递归  LeetCode 第405题
        给定一个整数，编写一个算法将这个数转换为十六进制数。
        对于负整数，我们通常使用补码运算方法

        给定一个整数，转换成任意进制表示的字符串格式
        769  转换成  字符串 769
        str = "0123456789"
        769/10    =   76  余  9
        76/10     =   7   余  6
        7/10      =   0   余  7

        str[9] + str[6] + str[7]

# 2,8,10,16 进制

def to_str(num,base):
    convert_str = "0123456789ABCDEF"
    if num < base:
        return convert_str[num]
    else:
        return to_str(num//base,base) + convert_str[num%base]

print(to_str(769,10))
print(to_str(769,2))
print(to_str(769,8))
print(to_str(769,16))


301
3*16^2 + 0 + 1*16^0

1401
1*8^3 + 4*8^2 + 0 + 1*8^0


# 967   =>    769    栈   后进先出

     ------------
底        967      顶    769
     ------------

可以用栈的方式实现递归

'''
from pythonds.basic.stack import Stack
s = Stack()

def to_str(num,base):
    convert_str = "0123456789ABCDEF"
    while num > 0:
        if num < base:
            s.push(convert_str[num])
        else:
            s.push(convert_str[num%base])
        num = num//base
    result = ""
    while not s.isEmpty():
        result = result + s.pop()
    return result

print(to_str(769,16))