import turtle as t

# правило: (F → F−F+F+FF−F−F+F)
# угол: 90°
# Здесь F означают «рисуем отрезок», + означает «повернуть вправо на угол», а − означает «повернуть влево на угол».

def curve_minkowski(length: float, iterations: int):
    if iterations == 0:
        t.forward(length * 4)
    else:
        curve_minkowski(length / 4, iterations - 1)
        t.left(90)
        curve_minkowski(length / 4, iterations - 1)
        t.right(90)
        curve_minkowski(length / 4, iterations - 1)
        t.right(90)
        curve_minkowski(length / 4, iterations - 1)
        curve_minkowski(length / 4, iterations - 1)
        t.left(90)
        curve_minkowski(length / 4, iterations - 1)
        t.left(90)
        curve_minkowski(length / 4, iterations - 1)
        t.right(90)
        curve_minkowski(length / 4, iterations - 1)


def start(x: float):
    t.clear()
    t.speed(1000)
    t.penup()
    x = x if x < 0 else -x
    t.goto(x, 0)
    t.pendown()

    ITERATION = 3  # номер итерации

    curve_minkowski(LENGTH, ITERATION)

    t.exitonclick()  # функция чтобы программа не завершалась сразу


LENGTH = 100  # длина линии

start(LENGTH * 2)
