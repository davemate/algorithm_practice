class Node:
    data = 0
    left = None
    right = None

    def __init__(self, val):
        self.data = val

    def Node(self, num):
        self.data = num


class Tree:
    root = None

    def __init__(self, node):
        self.root = node

    def addNode(self, node):
        iterNode = self.root
        while iterNode is not None:
            if node.data < iterNode.data:
                if iterNode.left is not None:
                    iterNode = iterNode.left
                else:
                    iterNode.left = node
                    return
            else:
                if iterNode.right is not None:
                    iterNode = iterNode.right
                else:
                    iterNode.right = node
                    return

    def printTreeInOrder(self, root):
        if root is not None:
            self.printTreeInOrder(root.left)
            print root.data
            self.printTreeInOrder(root.right)

    def printTreePostOrder(self, root):
        if root is not None:
            self.printTreePostOrder(root.left)
            self.printTreePostOrder(root.right)
            print root.data

    def printTreePreOrder(self, root):
        if root is not None:
            print root.data
            self.printTreePreOrder(root.left)
            self.printTreePreOrder(root.right)


tree = Tree(Node(10))
tree.addNode(Node(11))
tree.addNode(Node(2))
tree.addNode(Node(1))
tree.addNode(Node(5))
tree.addNode(Node(3))
tree.addNode(Node(4))
tree.addNode(Node(6))
tree.printTreeInOrder(tree.root)
tree.printTreePostOrder(tree.root)
tree.printTreePreOrder(tree.root)
