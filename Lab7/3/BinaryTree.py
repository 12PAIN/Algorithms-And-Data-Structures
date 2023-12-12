
class BinaryTree:
    def __init__(self, key, value=None, root=None):
        self.root: BinaryTree | None = root
        self.key = key
        self.value = value
        self.leftChild: BinaryTree | None = None
        self.rightChild: BinaryTree | None = None

    def insertLeft(self, newNodeKey):

        t = BinaryTree(newNodeKey, root=self)

        if self.leftChild is None:
            self.leftChild = t
        else:
            self.leftChild.root = t
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNodeKey):

        t = BinaryTree(newNodeKey, root=self)

        if self.rightChild is None:
            self.rightChild = t
        else:
            self.rightChild.root = t
            t.rightChild = self.rightChild
            self.rightChild = t
