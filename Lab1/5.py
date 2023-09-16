import timeit as timeit
import matplotlib.pyplot as plt
import numpy as np

def testInOperator(arr):
    return "test" in arr


x = list(range(1,11))

lists = list()
sets = list()

for i in range(1, 11):
    lists.append(list(range(1, 1000000*i)))
    sets.append(set(range(1, 1000000*i)))

y_1 = []
y_2 = []


for i in range(0,10):
    y_1.append(timeit.timeit(f'testInOperator(lists[{i}])', number=5, globals=globals()))
    y_2.append(timeit.timeit(f'testInOperator(sets[{i}])', number=5, globals=globals()))
        

fig = plt.figure()   # Создание объекта Figure
print (fig.axes)   # Список текущих областей рисования пуст
print (type(fig))   # тип объекта Figure

line1 = plt.plot(x,y_1, color="blue", linewidth=3, label="Lists")
line2 = plt.plot(x,y_2, color="red", linewidth=5, label="Sets")
plt.legend()

plt.ylabel("Time")
plt.xlabel("Elements, Mils")

print (fig.axes)

plt.show()