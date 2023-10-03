import random
import turtle



def tree(branchLen, t, line_width):
    if branchLen > 5:

        t.width(line_width)
        if branchLen == 15:
            t.color('green')
        else:
            t.color('brown')

        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t, line_width-1)
        t.left(40)
        tree(branchLen - 15, t, line_width-1)
        t.right(20)



        t.backward(branchLen)
        t.color('brown')





def main():

    t = turtle.Turtle()
    t.speed(1000)
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
