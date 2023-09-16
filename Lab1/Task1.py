import matplotlib.pyplot as plt
import numpy as np
import timeit as timeit
import random as rnd

def foo(a):
 for i in range(len(a), 0, -1):
    for j in range(1, i):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
 return a

#a = [1, 2, 3, 4, 2, 1, 3, 4, 3, 5, -2, -2, 2, -2, 65, 2, 2]
#foo(a)

#СОРТИРОВКА ОТ БОЛЬШЕГО К МЕНЬШЕМУ
#ВЫЧИСЛ. СЛОЖНОСТЬ N^2

fig = plt.figure()
print (fig.axes)  
print (type(fig))


x =2
elems = []
time_tmp = []

for i in range(1,45):
    arr = [rnd.randint(-100,100) for i in range(1,x)]
    elems.append(x)
    x = x+250
    time_print=timeit.timeit("foo(arr)", number=1, globals=globals())
    print(time_print, "\n")
    time_tmp.append(time_print)

plt.ylabel("Elements")
plt.xlabel("Time")

plt.plot(time_tmp,elems)

print (fig.axes)

plt.show()