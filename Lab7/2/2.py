from BinaryTreeWithDuplicates import BinaryTree as BinaryTreeWithDuplicates
from BinaryTreeWithoutDuplicates import BinaryTree as BinaryTreeWithoutDuplicates

def has_no_duplicates(tree: BinaryTreeWithDuplicates | BinaryTreeWithoutDuplicates):

    if tree.rightChild is None and tree.leftChild is None:
        return [tree.key]

    leftKeys = []
    if tree.leftChild is not None:
        leftKeysTmp = has_no_duplicates(tree.leftChild)

        if not leftKeysTmp:
            return False
        else:
            leftKeys += leftKeysTmp

    rightKeys = []
    if tree.rightChild is not None:
        rightKeysTmp = has_no_duplicates(tree.rightChild)

        if not rightKeysTmp:
            return False
        else:
            rightKeys += rightKeysTmp

    if (len(leftKeys) + len(rightKeys) + 1) != len(set(leftKeys + rightKeys + [tree.key])):
        return False
    elif tree.root is not None:
        return leftKeys + rightKeys + [tree.key]
    elif tree.root is None:
        return True


btwithd = BinaryTreeWithDuplicates(1, 10)
btwithd.insertLeft(2, 15)
btwithd.insertLeft(4, 15)
btwithd.insertRight(3, 20)
btwithd.insertRight(3, 21)

print("Есть ли дупликации в дереве(с возможными дублированиями)?:", has_no_duplicates(btwithd))


btwithoutd = BinaryTreeWithoutDuplicates(1,10)
btwithoutd.insertLeft(2, 15)
btwithoutd.insertLeft(4, 15)
btwithoutd.insertRight(3, 20)
btwithoutd.insertRight(3, 21)

print("Есть ли дупликации в дереве(с невозможными дублированиями)?:", has_no_duplicates(btwithoutd))
