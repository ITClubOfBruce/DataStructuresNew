# python 数据结构的性能

# 列表 List
# my_list = [1,2,3,4,5,6]
''' 
    1. 索引和分派到一个索引位置这两个操作，无论列表有多大，操作花费的时间都相同，O(1)
        print(my_list[0])
        print(my_list[5])
    
    2. 扩充list，append  也是O(1)
 '''
# import timeit
# from timeit import Timer

# def test1():
#     my_list = []
#     for i in range(1000):
#         my_list = my_list + [i]

# def test2():
#     my_list = []
#     for i in range(1000):
#         my_list.append(i)

# def test3():
#     my_list = [i for i in range(1000)]

# def test4():
#     my_list = list(range(1000))

# t1 = Timer("test1()","from __main__ import test1")
# print("连接",t1.timeit(number=1000),"seconds")
# t2 = Timer("test2()","from __main__ import test2")
# print("append",t2.timeit(number=1000),"seconds")
# t3 = Timer("test3()","from __main__ import test3")
# print("[]",t3.timeit(number=1000),"seconds")
# t4 = Timer("test4()","from __main__ import test4")
# print("list range",t4.timeit(number=1000),"seconds")

'''
    ----------- 测试pop()和pop(0) -----------
    pop()   O(1)
    pop(i)  O(n)
'''
# l = list(range(2000000))
# pop_zero = Timer("l.pop(0)","from __main__ import l")
# print("pop_zero",pop_zero.timeit(number=1000),"seconds")

# l = list(range(2000000))
# pop_end = Timer("l.pop()","from __main__ import l")
# print("pop_end",pop_end.timeit(number=1000),"seconds")

'''
    insert(i,item)      O(n)
    reverse  O(n)
    sort()  O(nlog n)
'''



'''
    字典 Dict
    除了复制和迭代是O(n)；in(包含)  删除，访问，复制都是 O(1)
    字典的包含关系始终比列表快
'''


'''
    list.pop(0)      O(n)
    list.pop()       O(1)
    list.append()    O(1)
    list[10]         O(1)


    for i in range(n):   O(n)

    k = 2 + 2   O(1)

    i = n
    while i > 0:   O(n)
        k = 2+2    
        i = i//2   
'''
'''
   作业：验证列表索引操作是O(1),并将时间复杂度改为O(n)
'''