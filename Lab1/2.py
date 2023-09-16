import random
import timeit as timeit
from math import inf
from heapq import nlargest
import matplotlib.pyplot as plt
import numpy as np


def mutableThreeMaximums(arr):
    idx1 = max(range(len(arr)), key=arr.__getitem__)
    max1 = arr[idx1]

    del arr[idx1]

    idx2 = max(range(len(arr)), key=arr.__getitem__)
    max2 = arr[idx2]

    del arr[idx2]

    idx3 = max(range(len(arr)), key=arr.__getitem__)
    max3 = arr[idx3]

    arr.insert(idx2, max2)
    arr.insert(idx1, max1)

    return [max1, max2, max3]


def npPartitionSort(arr):
    arr_np = np.array(arr)

    idx_max = max(range(len(arr)), key=arr.__getitem__)

    # res_np_part = -np.partition(-arr_np, 3)[:3]
    res_np_part = np.partition(arr_np, (-3, -3))[:-4:-1]

    return [res_np_part[0], res_np_part[1], res_np_part[2]]


def threeMaximums(arr):
    max1 = -inf
    max2 = -inf
    max3 = -inf

    for i in range(0, len(arr)):

        if arr[i] > max1:
            max3 = max2
            max2 = max1
            max1 = arr[i]

        elif arr[i] > max2:

            max3 = max2
            max2 = arr[i]

        elif arr[i] > max3:
            max3 = arr[i]

    return [max1, max2, max3]


def nlargestThreeMaximums(arr):
    return nlargest(3, arr)

def sortedThreeMaximums(arr):
    return sorted(arr, reverse=True)[:3]

def generateListOfNRandomElements(n):
    arr = []
    for i in range(0, n):
        arr.append(random.randint(-1 * n, n))

    return arr



x = []
data = []

for i in range(1, 11):
    x.append(i * 10000)
    data.append(generateListOfNRandomElements(i * 10000))

y_1 = []
y_2 = []
y_3 = []
y_4 = []
y_5 = []

for i in range(0, 10):
    y_1.append(timeit.timeit(f'npPartitionSort(data[{i}])', number=10, globals=globals()))
    y_2.append(timeit.timeit(f'nlargestThreeMaximums(data[{i}])', number=10, globals=globals()))
    y_3.append(timeit.timeit(f'mutableThreeMaximums(data[{i}])', number=10, globals=globals()))
    y_4.append(timeit.timeit(f'threeMaximums(data[{i}])', number=10, globals=globals()))
    y_5.append(timeit.timeit(f'sortedThreeMaximums(data[{i}])', number=10, globals=globals()))

fig = plt.figure()  # Создание объекта Figure
print(fig.axes)  # Список текущих областей рисования пуст
print(type(fig))  # тип объекта Figure

line1 = plt.plot(x, y_1, color="blue", linewidth=3, label="Sort with NP partition method")
line2 = plt.plot(x, y_2, color="red", linewidth=3, label="Heapq nlargest")
line3 = plt.plot(x, y_3, color="green", linewidth=3, label="Mutable three maximums")
line4 = plt.plot(x, y_4, color="brown", linewidth=3, label="Custom algorithm")
line5 = plt.plot(x, y_5, color="orange", linewidth=3, label="Sorted")
plt.grid()
plt.legend()

plt.ylabel("Time")
plt.xlabel("Elements")

print(fig.axes)

plt.show()