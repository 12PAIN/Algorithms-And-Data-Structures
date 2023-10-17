from lists.Stack import Stack


def stackCalculator(expression):
    stack = Stack()
    expArray = list(expression)
    for i in range(len(expArray)):
        if expArray[i] == "+":
            stack.push(stack.pop() + stack.pop())
        elif expArray[i] == "-":
            stack.push(stack.pop() - stack.pop())
        elif expArray[i] == "*":
            stack.push(stack.pop() * stack.pop())
        elif expArray[i] == "/":
            stack.push(stack.pop() / stack.pop())
        else:
            stack.push(int(expArray[i]))
    return stack.pop()


try:
    print(stackCalculator('12*'))
except Exception as e:
    print("Выражение составлено некорректно")
