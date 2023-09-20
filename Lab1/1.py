import random
import timeit as timeit
import matplotlib.pyplot as plt

#Сумма целых цифр в строке
#Сложность: O(n)
def foo(s): # s - строка
    val = 0
    for c in s:
        if c.isdigit():
            val += int(c)
    return val

# def generateStringOfNumbers(N):
#     return str(10**(N-1))

def generateStringOfNumbers(N):
    return "1" * N

x = []
y = []

for i in range(1000, 100000, 1000):
    x.append(i)
    generatedStr = generateStringOfNumbers(i)
    time = timeit.timeit('foo(generatedStr)', number=5, globals=globals())
    y.append(time)

fig = plt.figure()  # Создание объекта Figure
print(fig.axes)  # Список текущих областей рисования пуст
print(type(fig))  # тип объекта Figure

plt.plot(x, y)

plt.ylabel("Time, x1")
plt.xlabel("N, string length")

print(fig.axes)

plt.show()
