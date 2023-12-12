from BinaryTree import BinaryTree
import re

def buildParseTree(tokens):

    tree = BinaryTree(None)
    currentNode = tree

    for token in tokens:

        if token == "(":
            currentNode.insertLeft(None)
            currentNode = currentNode.leftChild
            continue

        if token in "|&":
            currentNode.key = token
            currentNode.insertRight(None)
            currentNode = currentNode.rightChild
            continue

        if token == "!":
            currentNode.key = token
            currentNode.insertLeft(None)
            currentNode = currentNode.leftChild
            continue

        if token in ["True", "False"]:

            currentNode.key = token
            currentNode = currentNode.root if currentNode.root is not None else currentNode

            if currentNode.key == "!":
                currentNode = currentNode.root if currentNode.root is not None else currentNode

            continue

        if token == ")":
            currentNode = currentNode.root
            if currentNode is not None:
                if currentNode.key == "!":
                    currentNode = currentNode.root if currentNode.root is not None else currentNode
            continue


    return tree

def solve(tree: BinaryTree):
    if tree.leftChild is None and tree.rightChild is None:
        return tree.key

    leftResult = solve(tree.leftChild)
    rightResult = solve(tree.rightChild) if tree.rightChild is not None else None

    if tree.key == "|":
        return "True" if leftResult == "True" or rightResult == "True" else "False"

    if tree.key == "&":
        return "True" if leftResult == "True" and rightResult == "True" else "False"

    if tree.key == "!":
        return "True" if leftResult == "False" else "False"

def printExp(tree):

    if tree.leftChild is None and tree.rightChild is None:
        return tree.key

    if tree.rightChild is not None:
        st = f'( {printExp(tree.leftChild)} {tree.key} {printExp(tree.rightChild)} )'
    else:
        st = f'!{printExp(tree.leftChild)}'

    return st

def evaluate(exp):

    tokens = re.findall("True|False|[()]|[|&!]", exp)
    # print(tokens)
    tree = buildParseTree(tokens)
    print(printExp(tree))
    return solve(tree)


expression = input("Введите выражение ->")

print(evaluate(expression))
