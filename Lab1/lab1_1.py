import os


import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()   # Создание объекта Figure
print (fig.axes)   # Список текущих областей рисования пуст
print (type(fig))   # тип объекта Figure

lag=0.1
x=np.arange(0.0,50,lag)
y=3*x

plt.plot(x,y)

plt.ylabel("y-axis")
plt.xlabel("x-axis")

#plt.scatter(1.0, 1.0)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)

# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области
print (fig.axes)

plt.show()