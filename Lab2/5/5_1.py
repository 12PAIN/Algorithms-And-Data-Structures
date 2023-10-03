import turtle



def tree(branchLen, t, line_width):
    t.width(line_width)
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t, line_width-1)
        t.left(40)
        tree(branchLen - 15, t, line_width-1)
        t.right(20)
        t.backward(branchLen)



def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.width(6)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t, 6)
    myWin.exitonclick()


main()
