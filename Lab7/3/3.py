from BinaryTree import BinaryTree
import pickle


def animalsGame(tree: BinaryTree):
    currentNode: BinaryTree = tree

    if tree.leftChild is None and tree.rightChild is None:
        tree.key = "Это млекопитающее?"
        print("Загадайте одно млекопитающее и не млекопитающее")

        animal1 = input("Введите млекопитающее->")
        animal2 = input("Введите не млекопитающее->")

        tree.insertLeft(animal1)
        tree.insertRight(animal2)


    while currentNode.leftChild is not None and currentNode.rightChild is not None:

        print(currentNode.key)
        answer = input("Введите да/нет ->").lower()

        if answer == "да":
            currentNode = currentNode.leftChild
        if answer == "нет":
            currentNode = currentNode.rightChild

    print("Вы загадали", currentNode.key, "?")
    answer = input("Введите да/нет ->").lower()

    if answer == "нет":
        animal = input("Какое животное вы загадали? ->")
        question = input(f'Какой вопрос поможет отличить {animal} от {currentNode.key}? ->')

        t = currentNode.key
        currentNode.key = question
        currentNode.insertLeft(animal)
        currentNode.insertRight(t)

    with open('tree.pickle', 'wb') as handle:
        pickle.dump(tree, handle)
    return


with open('tree.pickle', 'rb') as handle:
    programDataBase = pickle.load(handle)
    animalsGame(programDataBase)

# programDataBase = BinaryTree(None)
# animalsGame(programDataBase)
