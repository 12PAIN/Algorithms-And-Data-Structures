import random
import turtle



def tree(branchLen, t, line_width):
    if branchLen >= 5:

        angle = random.randint(8, 25) if branchLen > 45 else random.randint(25, 45)
        branchLenDiff = random.randint(3, 15)

        t.width(line_width)
        if line_width <= 2:
            t.color('green')
        else:
            t.color('brown')

        t.forward(branchLen)

        random_peek = random.randint(1,2)
        if random_peek == 1:
            t.right(angle)
            tree(branchLen - branchLenDiff, t, line_width - 1 if line_width >= 2 else 1)
        else:
            t.left(angle)
            tree(branchLen - branchLenDiff, t, line_width - 1 if line_width >= 2 else 1)

        if random_peek == 2:
            angle2 = random.randint(20, 30) if branchLen > 50 else random.randint(30, 50)
            t.right(angle2)
            tree(branchLen - branchLenDiff, t, line_width - 1 if line_width >= 2 else 1)
            t.left(angle2 - angle)
        else:
            angle2 = random.randint(20, 30) if branchLen > 50 else random.randint(30, 50)
            t.left(angle2)
            tree(branchLen - branchLenDiff, t, line_width - 1 if line_width >= 2 else 1)
            t.right(angle2 - angle)

        if line_width <= 2:
            t.color('green')
        else:
            t.color('brown')


        t.backward(branchLen)



def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.color('brown')
    t.width(10)
    t.left(90)
    t.speed(100000)
    t.up()
    t.backward(200)
    t.down()
    tree(90, t, 10)
    myWin.exitonclick()


main()
