# 注册牛客网，LeetCode(必刷)

# 如果a+b+c = 1000，并且a^2 + b^2 = c^2，求出所有的a,b,c可能的组合
# 解决同一个问题，时间短的算法更好

# 第一种算法，三重循环
# import time

# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()

# print("运行时间为:%f"%(end_time - start_time))

'''
    a,b,c:0,500,500
    a,b,c:200,375,425
    a,b,c:375,200,425
    a,b,c:500,0,500
    运行时间为:136.097976
'''

# 为了让执行时间更短，提出第二种算法，双重循环

# import time
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()

# print("执行的时间是：%f"%(end_time - start_time))

'''
    a,b,c:0,500,500
    a,b,c:200,375,425
    a,b,c:375,200,425
    a,b,c:500,0,500
    执行的时间是：1.118624
'''


# 思考：都可以从哪些角度去优化程序




'''
    1. 什么是算法？
       算法是独立存在的一种解决问题的方法和思想！！！
    2. 算法的五大特性
       输入：算法具有0个或者多个输入；
       输出：算法至少有1个或者多个输出；
       有穷性：算法在有限的步骤之后会自动结束而不会无限循环，
       并且每一个步骤可以在可接受的时间内完成；
       确定性：算法中的每一步都有确定的含义，不会出现二义性
       可行性：算法的每一步都是可行的（每一步都能够执行有限的次数完成）
    3. 算法效率衡量
       实现算法程序的执行时间可以反应出来算法的效率
       单纯依靠运行时间来比较算法的优劣不一定是客观准确的（程序的运行离不开计算机环境，所以和硬件，操作系统）
    4. 最终算法用什么去衡量？
       时间复杂度
    5. 表示法：大O记法
       假设计算机执行算法每个基本操作的时间是固定的一个时间单位，那么有多少个基本操作就代表会花费多少时间单位，
       虽然对于不同的机器环境而言，确切的时间单位是不同的，但是对于算法进行多少个基本操作在规模数量级上是相同的
       因此，可以忽略机器环境的影响而客观的反应算法的时间效率
       对于算法的时间效率，用“大O记法”
       O(n^3)       100n^2     10000n^2   
       O(n^2)
    6. 时间复杂度分类
       最优时间复杂度：算法完成工作最少需要多少基本操作（过于理想化，没什么参考价值）
       最坏时间复杂度：。。。。最多。。。（提供了一种保证，表明算法在此程度的基本操作中一定能完成工作）
       平均时间复杂度：。。。。平均。。。。（对算法整体一个全面的评价，但是这种衡量方式没有保证）

      我们关注算法的最坏情况！！！ ———> 最坏时间复杂度

    7. 时间复杂度的几条基本计算规则
       基本操作，也就是只有常数项，认为其时间复杂度为O(1)
       顺序结构，时间复杂度按加法进行计算
       循环结构，时间复杂度按乘法进行计算
       分支：取最大值
       判断一个算法的效率时，只需要关注操作数量的最高次项，其他次要项和常数项可以忽略
       没有特殊情况下，我们分析的都是最坏时间复杂度
    8. 练习
       12                                            O(1)
       2n+3                                          O(n)
       3n^2 + 2n + 1                                 O(n^2)
       5logn + 20                                    O(logn)
       2n + 5nlogn + 20                              O(nlogn)
       100000n^2 + 2*n^3 + 4                         O(n^3)
       2^n                                           O(2^n)

      O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
    
    
    9.  练习：求前n个正整数的和 (高斯算法)
       
'''
# import time

# def sum_of_n(n):
#    start_time = time.time()
#    the_sum = 0
#    for i in range(1,n+1):
#       the_sum = the_sum + i

#    end_time = time.time()
#    return the_sum,end_time-start_time


# print(sum_of_n(100000000))


# def sum_of_n_2(n):

#    return (n*(n+1))/2
# start = time.time()
# print(sum_of_n_2(100000000))
# end = time.time()
# print(end - start)

'''
   练习：编写函数求出列表中的最小值，
   要求：函数1：O(n^2)    两两比较
         函数2：O(n)      设置一个临时变量，更优化的算法就是把这个临时变量设置成列表中的第一个元素
'''

my_list = [10,40,9,6,8,100]


def getMin(source_list):
    #两层循环，数量级是n²
   for i in range(len(source_list)):
      for j in range(len(source_list)):
         #拿第i个数，和其他所有的数进行比较，如果遇到比自己小的，
         #就说明自己不是最小的，也就不用继续比下去了,break退出当前循环
         if source_list[i] > source_list[j]: 
            break
        #如果没有从break出口出去，就说明没有遇到比自己小的
        #自己就是最小的，所有要返回当前数字
      else:
         return  source_list[i]
print(getMin(my_list))


def get_min2(my_list):
   min_num = my_list[0]
   for i in range(len(my_list)):
      if my_list[i] < min_num:
         min_num = my_list[i]
   return min_num

print(get_min2(my_list))