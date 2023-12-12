
class BinaryTree:
    def __init__(self, key, value=None, root=None):
        self.root: BinaryTree | None = root
        self.key = key
        self.value = value
        self.leftChild: BinaryTree | None = None
        self.rightChild: BinaryTree | None = None

    def find(self, key):

        if self.key == key:
            return self
        elif self.leftChild is None and self.rightChild is None:
            return None

        leftResult = None
        if self.leftChild is not None:
            leftResult = self.leftChild.find(key)

        rightResult = None
        if self.rightChild is not None:
            rightResult = self.rightChild.find(key)


        result = leftResult if leftResult is not None else rightResult

        return result

    def insertLeft(self, newNodeKey, newNodeValue=None):


        findResult = self.find(newNodeKey)
        if findResult is not None:
            findResult.value = newNodeValue
            return


        t = BinaryTree(newNodeKey, value=newNodeValue, root=self)

        if self.leftChild is None:
            self.leftChild = t
        else:
            self.leftChild.root = t
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNodeKey, newNodeValue=None):

        findResult = self.find(newNodeKey)
        if findResult is not None:
            findResult.value = newNodeValue
            return

        t = BinaryTree(newNodeKey, value=newNodeValue, root=self)

        if self.rightChild is None:
            self.rightChild = t
        else:
            self.rightChild.root = t
            t.rightChild = self.rightChild
            self.rightChild = t
