import sys
sys.setrecursionlimit(1000000)

root = None

class Node:
    def build(p, b):
        root = Node(0, 1, b[1])
        for i in range(2, len(b)): root.addXNode(Node(p[i], i, b[i]))
        return root

    def __init__(self, pX, x, b):
        print(str(pX) + "> Node " + str(x))
        self.pX = pX
        self.x = x
        self.b = b
        self.g = 0
        self.h = 0
        self.children = []

    
    def addXNode(self, node):
        if node.pX == self.x:
            self.addNode(node)
        else:
            for child in self.children:
                child.addXNode(node)
    
    def addNode(self, node):
        self.children.append(node)

    def addXGrowth(self, x, v):
        if x in [child.x in self.children]:
            
            self.addGrowth(v)
        else:
            for child in self.children: child.addXGrowth(x, v)
    
    def addGrowth(self, v):
        self.g += v
        for child in self.children: child.addGrowth(v)

    def addXHarvest(self, x, v):
        if self.x == x:
            self.addHarvest(v)
        else:
            for child in self.children: child.addXHarvest(x, v)
    
    def addHarvest(self, v):
        self.h += v
        for child in self.children: child.addHarvest(v)
    
def solve(o):
    (t, x, v) = o[-1]
    if t == 1:
        root.addXGrowth(x, v)
    else:
        root.addXHarvest(x, v)

    

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        sArr = input().split(" ")
        n = int(sArr[0])
        q = int(sArr[1])
        p = [int(s) for s in input().split(" ")]
        b = [int(s) for s in input().split(" ")]

        o = []
        for iQ in range(q):
            sArr = input().split(" ")
            t = int(sArr[0])
            x = int(sArr[1])
            v = int(sArr[2])
            o.append((t, x, v))
        
        p.insert(0, 0)
        p.insert(1, 0)
        b.insert(0, 0)
        root = Node.build(p, b)

        solve(o)
        print()

