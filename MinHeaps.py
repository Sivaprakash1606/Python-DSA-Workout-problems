class HeapNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class MinHeap:
    def __init__(self):
        self.root=None
    def add(self,data):
        if not self.root:
            self.root=HeapNode(data)
            return
    self.recursive_add(data,self.root)
    def recursive_add(self,data,node):
        if not node.left:
            node.left=HeapNode(data)
        elif not node.right:
            node.right=HeapNode(data)

    def get_count(self,node):
        if node node:
            return 0
        return 1+self.get_count(node.left)+self.get_count(node.right)





heap=MinHeap()
heap.add(10)

