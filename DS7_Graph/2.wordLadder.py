'''
    LeetCode 第1203题: 项目管理问题
一、问题描述
    字梯问题：将单词'FOOL' 转换为单词 'SAGE'。
    前提条件：每一步必须将一个字符转换成另一个字
    举例：FOOL 
         POOL
         POLL
         POLE
         PALE
         SALE
         SAGE
    目的：计算从FOOL到SAGE所需要的最小转换次数 
    有的会给定特定的单词列表，比如5000单词量
    将一个字与列表中的每个其他词进行比较O(n^2) 5000^2 = 25000000
    步骤：
    1. 将字之间的关系表示成图 （无向图，边未加权）
    2. 使用广度优先搜索的图算法来找到从开始字到结束字的有效路径


         _OOL   F_OL   FO_L   FOO_
         AOOL   FAOL   FOPL   FOOA
    实现：用字典实现
    key:  _OOL   F_OL   FO_L   FOO_
    value: 对应的单词列表
    {
        '_OOL':[AOOL,...],
        'F_OL':[FAOL,...],
        'FO_L':[FOPL,...],
        'FOO_':[FOOA,...]
    }
'''
from pythonds.graphs import Graph


# 顶点
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    lines = wfile.readlines()
    for line in lines:
        word = line.strip('\n')
        for i in range(len(word)):
            bucket = word[:i] + "_" +word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

wordFile = './DS7_Graph/word.txt'
print(buildGraph(wordFile).getVertices())

