import random
import turtle as t

# def draw(length: float, iterations: int, goto_x, goto_y):
#     if iterations != 0:
#         t.goto(goto_x, goto_y)
#         t.left(60)
#         t.forward(length)
#         t.right(120)
#         t.forward(length)
#         t.right(120)
#         t.forward(length)
#         t.right(180)
#         draw(length * random.uniform(0.8, 1.6), iterations-1, goto_x+(length * random.uniform(0.2, 0.4)), goto_y)


def draw(length: float, iterations: int, goto_x, goto_y):
    if iterations != 0:
        # t.goto(goto_x, goto_y)
        t.left(60)
        t.forward(length)
        t.right(120)
        t.forward(length * random.uniform(0.4, 0.9) + 40)
        t.left(60)
        draw(length * random.uniform(0.7, 1.4), iterations-1, goto_x+(length * random.uniform(0.2, 0.4)), goto_y)

def start(x: float):
    t.clear()
    t.penup()
    x = x if x < 0 else -x
    t.goto(x, -200)
    t.pendown()

    ITERATION = 7  # номер итерации

    draw(LENGTH, ITERATION, x, -250)

    t.exitonclick()  # функция чтобы программа не завершалась сразу


LENGTH = 250  # длина линии

start(-400)
