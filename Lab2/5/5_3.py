import random
import turtle



def tree(branchLen, t, line_width):
    if branchLen > 5:

        angle = (random.randint(10, 40) + 5) * 1.1

        t.width(line_width)
        if branchLen == 15:
            t.color('green')
        else:
            t.color('brown')

        t.forward(branchLen)
        t.right(angle)
        tree(branchLen - 15, t, line_width-1)
        t.left(angle * 2)
        tree(branchLen - 15, t, line_width-1)
        t.right(angle)



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
