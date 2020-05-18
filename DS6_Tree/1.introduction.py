'''
    重点：二叉树的前序，中序，后序遍历
    LeetCode：144题，94题，145题

一、树相关的概念：
    例子：html文档
    节点：节点是树的基本部分，也可以叫做“键”。节点可以由附加信息。这个附加信息叫做“有效载荷”
    边：边是树的另一个基本部分。边连接两个节点以显示它们之间存在关系。
       每个节点（除了根之外）都恰好从另一个节点传入连接。每个节点可以具有多个输出边
    根：树的根是树中唯一没有传入边的节点
    路径：路径是由边连接节点的有序列表
    子节点：具有来自相同传入边的节点C的集合称为该节点的子节点
    父节点：具有和它相同传入边的所连接的节点为父节点
    兄弟：树中作为同一父节点的子节点的节点被称为兄弟节点
    子树：子树是父节点和该节点的所有后代组成的一组节点和边
    叶节点：叶节点是没有子节点的节点
    层数：节点n的层数为从根节点到该节点所经过的分支数目
    高度：树的高度等于树中任何节点的最大层数

二、树的定义：
    定义一：树由一组节点和一组连接节点的边组成
        树的一个节点被指定为根节点
        除了根节点之外，每个节点n通过一个其他节点p的边连接，其中p是n的父节点
        从根路径遍历到每个节点路径唯一
        如果树中的每个节点最多有两个子节点，我们说概述是一个“二叉树”
    定义二（递归定义）：
        树是空的，或者由一个根节点和0个或者多个子树组成，每个子树也是一棵树。每个子树的节点通过
        边连接到父树的根节点。

三、树的表示
   1. 列表表示 ['html',
        ['head' ['title',[],[]],['meta',[],[]]]
        ['body' [''],[]]
   ]
   2. 节点表示（抽象ADT）:使用节点和引用，定义一个具有根值属性的类和左子树，右子树
    
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp
    
    # 插入右子树
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())


四、分析树（使用树数据结构解决问题：字符串和数学计算问题）
如何从带有完全括号的数学表达式 ( (7+3) * (5-2) )去构建分析树？
怎么放入？
怎么取出？
# 分析：根节点，左子树，右子树
第一步：把表达式字符串拆分成符号列表。四种：左括号，右括号，运算符，操作数
      读到一个左括号：开始一个新的表达式，树对应表达式的话，此时应当创建一个新的树
      读到一个右括号：结束了一个表达式
      操作数是叶子节点，同时也是操作符的子节点
      每一个操作符都有一个左，右孩子
第二步：根据第一步的分析，定义规则
      如果当前符号是“(”,添加一个新节点作为当前节点的左子节点，并且下降到左子节点
      如果当前符号是列表['+','-','/','*']中，将当前节点的根值设置为由当前符号表示的运算法。添加一个新节点作为当前节点的右子节点，并下降到右子节点
      如果当前符号是数字，将当前节点的根值设置为该数字并返回父节点
      如果当前符号是“)”，则转到当前节点的父节点
'''
from pythonds.trees.binaryTree import BinaryTree



