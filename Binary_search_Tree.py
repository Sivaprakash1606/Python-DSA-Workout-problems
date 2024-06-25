# BinarySearchTree # BSTNode
# With Add, Remove, search

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = BSTNode(data)
        self.recursiveAdd(data, self.root)

    def recursiveAdd(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.recursiveAdd(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.recursiveAdd(data, node.right)

    def display(self):
        result = []
        self.inorderTraversal(self.root, result)
        print(result)

    def inorderTraversal(self, node, result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left, result)
            result.append(node.data)
            self.inorderTraversal(node.right, result)

    def remove(self, data):
        if self.root is None:
            print("It is a empty Tree")
            return

        if self.root.data == data:
            self.root = None
            return
        self.recursiveRemove(self.root, data)

    def recursiveRemove(self, node, data):
        if node.left and node.left.data == data:
            node.left = None
            return

        elif node.right and node.right.data == data:
            node.right = None
            return

        elif data < node.data:
            self.recursiveRemove(node.left, data)

        elif data > node.data:
            self.recursiveRemove(node.right, data)

    def search(self, data):

        node = self.recursiveSearch(self.root, data)

        if node:
            print("True")

        else:
            print("False")

    def recursiveSearch(self, node, data):
        if not node:
            return node

        if node and node.data == data:
            return node

        elif data < node.data:
            return self.recursiveSearch(node.left, data)

        elif data > node.data:
            return self.recursiveSearch(node.right, data)


BST = BinarySearchTree()
BST.add(45)
BST.add(10)
BST.add(50)
BST.add(9)
BST.add(11)
BST.add(46)
BST.add(51)
BST.display()
BST.remove(11)
BST.display()
BST.search(15)  