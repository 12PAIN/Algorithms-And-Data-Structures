import lists.UnorderedList as lst


def move_to_front(newStr, myList):

    if myList.search(newStr):
        myList.pop(myList.index(newStr))
    myList.add(newStr)


strList = lst.UnorderedList()

# :))))))
while 1 != 2:
    inpString = input()
    if inpString == '':
        break
    move_to_front(inpString, strList)
    print(strList)
