import random
import turtle



def tree(branchLen, t, line_width):
    if branchLen > 5:

        angle = (random.randint(10, 40) + 5) * 1.1
        branchLenDiff = random.randint(2, 12)+7

        t.width(line_width)
        if branchLen < 20:
            t.color('green')
        else:
            t.color('brown')

        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - branchLenDiff, t, line_width-1)
        t.left(angle * 2)
        tree(branchLen - branchLenDiff, t, line_width-1)
        t.right(angle)



        t.backward(branchLen)
        t.color('brown')





def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.color('brown')
    t.width(6)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75, t, 6)
    myWin.exitonclick()


main()
