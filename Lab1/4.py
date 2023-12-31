import timeit as timeit
import matplotlib.pyplot as plt
import numpy as np


def testDelOperatorLists(arr):
    del arr[0]


def testDelOperatorDicts(arr):
    del arr['' + str(1)]


x = list(range(100000, 1000001, 100000))

lists = []
dicts = []

for i in range(1, 11):
    lists.append(list(range(1, 100000 * i)))
    dicts.append( { str(j): j for j in range(1, 100000 * i) })

y_1 = []
y_2 = []

for i in range(0, 10):
    y_1.append(timeit.timeit(f'testDelOperatorLists(lists[{i}])', number=1, globals=globals()))
    y_2.append(timeit.timeit(f'testDelOperatorDicts(dicts[{i}])', number=1, globals=globals()))

fig = plt.figure()  # Создание объекта Figure
print(fig.axes)  # Список текущих областей рисования пуст
print(type(fig))  # тип объекта Figure

line1 = plt.plot(x, y_1, color="blue", linewidth=3, label="Lists")
line2 = plt.plot(x, y_2, color="red", linewidth=3, label="Dicts")
plt.legend()

plt.ylabel("Time")
plt.xlabel("Elements")

print(fig.axes)

plt.show()