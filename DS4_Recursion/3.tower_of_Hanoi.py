'''
    LeetCode 面试题08.06  汉诺塔问题
    在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
    (1) 每次只能移动一个盘子;
    (2) 盘子只能从柱子顶端滑出移到下一根柱子;
    (3) 盘子只能叠在比它大的盘子上。

    请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。



    递归：
    1. 找出最基础部分
    2. 无限向着最基础的部分靠近
    3. 递归函数


    第一步：找出最基础的部分；假设，N = 5，（1,2,3号杆），最初都在1号杆上。
    
    A号5    借助C号杆移4个到B号    剩1到3号  （A:1    B:4    C:0）
    B号4    借助A号杆移3个到C号  剩1到1号  （A:1    B:0    C:4）
            借助B号杆移2个到xx号
            借助x号杆移1个到xx号
    fromPole   从哪个杆
    withPole   借助哪个杆
    num        移动多少个
    toPole     到哪个杆
    move(num,fromPole,withPole,toPole)



def move(num,fromPole,withPole,toPole):
    if num >= 1:
        move(num-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        move(num-1,withPole,toPole,fromPole)

def moveDisk(fromPole,toPole):
    print("移动盘子从",fromPole,"到",toPole)


move(5,"A","B","C")

'''



'''
    迷宫：参考LeetCode1210题：穿过迷宫的最少移动次数

    1. 从初始位置尝试向上走一步，以此来开始递归
    2. 如果上面走不通则尝试走下面，再开始递归
    3. 上下都不通，走左边，再开始递归
    4. 上下左都不通，走右边，再开始递归


    四种基本情况：
    1. 碰到 “墙壁”, 方格被占用无法通行
    2. 方格被访问过，未避免陷入循环不在此位置继续寻找
    3. 碰到边缘，表示成功
    4. 四个方向探索失败，游戏失败
'''