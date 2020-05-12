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

    turtle  
    __init__  用来读取迷宫的数据，初始化迷宫内部，并找到游戏精灵的初始位置
    draw_maze  用来在屏幕上绘制迷宫
    update_position   用来更新迷宫内的状态和游戏精灵的位置
    is_exit  用来判断当前位置是否是出口

'''
# 迷宫的地图：从txt文件中获取,地图是一个只包含： +  空格的文件 

# 用到的绘制迷宫的符号：+  空格
# turtle   GUI库绘制迷宫地图

import turtle
self.wn = turtle.Screen()
class Maze:
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []

        mazeFile = open(mazeFileName,'r')
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'Q':
                    self.startRow = rowsInMaze
                    self.starCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        print(self.xTranslate)
        print(self.yTranslate)
        self.t = turtle.Turtle(shape='turtle')
        self.wn = turtle.Screen()
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)
        # self.wn.exitonclick()   
    # 绘制屏幕
    def draw_maze(self,x,y,color):
        self.t.up()
        self.t.goto(x-.5,y-.5)
        self.t.color('black',color)
        self.t.setheading(90)
        self.t.down
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()
        update()



mazeFileName = 'DS4_Recursion/maze.txt'
maze = Maze(mazeFileName)
maze.draw_maze(0,0,"red")


# import turtle
     
# PART_OF_PATH = 'O'
# TRIED = '.'
# OBSTACLE = '+'
# DEAD_END = '-'
     
# class Maze:
#     def __init__(self,mazeFileName):
#         rowsInMaze = 0
#         columnsInMaze = 0
#         self.mazelist = []
#         self.startRow = 0
#         self.startCol = 0
#         mazeFile = open(mazeFileName,'r')
#         rowsInMaze = 0
#         for line in mazeFile:
#             rowList = []
#             col = 0
#             for ch in line[:-1]:
#                 rowList.append(ch)
#                 if ch == 'S':
#                     self.startRow = rowsInMaze
#                     self.startCol = col
#                 col = col + 1
#             rowsInMaze = rowsInMaze + 1
#             self.mazelist.append(rowList)
#             columnsInMaze = len(rowList)
     
#         self.rowsInMaze = rowsInMaze
#         self.columnsInMaze = columnsInMaze
#         self.xTranslate = -columnsInMaze/2
#         self.yTranslate = rowsInMaze/2
#         self.t = turtle.Turtle()
#         self.t.shape('turtle')
#         self.wn = turtle.Screen()
#         self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5,-(rowsInMaze-1)/2-.5,(columnsInMaze-1)/2+.5,(rowsInMaze-1)/2+.5)
     
#     def drawMaze(self):
#         self.t.speed(10)
#         for y in range(self.rowsInMaze):
#             for x in range(self.columnsInMaze):
#                 if self.mazelist[y][x] ==OBSTACLE:
#                     self.drawCenteredBox(x+self.xTranslate,-y+self.yTranslate,'tan')
#         self.t.color('black','blue')
#         # self.t.fillcolor('blue')
     
#     def drawCenteredBox(self,x,y,color):
#         self.t.up()
#         self.t.goto(x-.5,y-.5)
#         self.t.color(color)
#         self.t.fillcolor(color)
#         self.t.setheading(90)
#         self.t.down()
#         self.t.begin_fill()
#         for i in range(4):
#             self.t.forward(1)
#             self.t.right(90)
#         self.t.end_fill()
     
#     def moveTurtle(self,x,y):
#         self.t.up()
#         self.t.setheading(self.t.towards(x+self.xTranslate,-y+self.yTranslate))
#         self.t.goto(x+self.xTranslate,-y+self.yTranslate)
     
#     def dropBreadcrumb(self,color):
#         self.t.dot(10,color)
     
#     def updatePosition(self,row,col,val=None):
#         if val:
#             self.mazelist[row][col] = val
#         self.moveTurtle(col,row)
     
#         if val == PART_OF_PATH:
#             color = 'green'
#         elif val == OBSTACLE:
#             color = 'red'
#         elif val == TRIED:
#             color = 'black'
#         elif val == DEAD_END:
#             color = 'red'
#         else:
#             color = None
     
#         if color:
#             self.dropBreadcrumb(color)
     
#     def isExit(self,row,col):
#         return (row == 0 or
#                 row == self.rowsInMaze-1 or
#                 col == 0 or
#                 col == self.columnsInMaze-1 )
     
#     def __getitem__(self,idx):
#         return self.mazelist[idx]
     
     
# def searchFrom(maze, startRow,startColumn):
#        # try each of four directions from this point until we find a way out.
#        # base Case return values:
#        #  1. We have run into anobstacle, return false
#     maze.updatePosition(startRow, startColumn)
#     if maze[startRow][startColumn] == OBSTACLE :
#         return False
#        #  2. We have found a square thathas already been explored
#     if maze[startRow][startColumn] == TRIED or maze[startRow][startColumn]== DEAD_END:
#         return False
#        # 3. We have found an outside edge not occupied by an obstacle
#     if maze.isExit(startRow,startColumn):
#         maze.updatePosition(startRow, startColumn, PART_OF_PATH)
#         return True
#     maze.updatePosition(startRow, startColumn, TRIED)
#        # Otherwise, use logical short circuiting to try each direction
#        # in turn (if needed)
#     found = searchFrom(maze, startRow-1, startColumn) or \
#             searchFrom(maze, startRow+1,startColumn) or \
#             searchFrom(maze, startRow,startColumn-1) or \
#             searchFrom(maze, startRow,startColumn+1)
#     if found:
#         maze.updatePosition(startRow, startColumn, PART_OF_PATH)
#     else:
#         maze.updatePosition(startRow, startColumn, DEAD_END)
#     return found
     
     
# myMaze = Maze('DS4_Recursion/maze.txt')
# myMaze.drawMaze()
# myMaze.updatePosition(myMaze.startRow,myMaze.startCol)
     
# searchFrom(myMaze, myMaze.startRow,myMaze.startCol)
