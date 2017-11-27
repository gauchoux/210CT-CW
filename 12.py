import sys
from collections import defaultdict

class undirectGraph(object):
    def __init__(self):
        self.adjDict = defaultdict(set)

    def addNode(self, node):
        self.adjDict[node]
        
    def addAdjNode(self, node, adjnode):
        self.adjDict[node].add(adjnode)
        
    def disp(self):
        dict = str(self.adjDict)
        dict = dict.replace("defaultdict(<class 'set'>, ","")
        print(dict)
        return self.adjDict


    
if __name__ == '__main__':
    g = undirectGraph()
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.addNode(5)
    g.addNode(6)
    g.addAdjNode(1,2)
    g.addAdjNode(1,6)
    g.addAdjNode(2,1)
    g.addAdjNode(3,6)
    g.addAdjNode(3,4)
    g.addAdjNode(4,3)
    g.addAdjNode(4,5)
    g.addAdjNode(5,4)
    g.addAdjNode(5,6)
    g.addAdjNode(6,1)
    g.addAdjNode(6,3)
    g.addAdjNode(6,5)
    g.disp()
