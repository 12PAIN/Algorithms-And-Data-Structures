import timeit as timeit
import matplotlib.pyplot as plt

x = [i for i in range(10, 41, 10)]
fib_time = []
fib_with_lucas_time = []

def fibonacci(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    if n < 0:
        return 0

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)

def lucas_with_fib(n):
    return fibonacci(n-1) + fibonacci(n+1)

def fib_with_lucas(n):
    i = n // 2
    j = n - i

    return ( ( fibonacci(i) + lucas_with_fib(j) )*( fibonacci(j) + lucas_with_fib(i) ) ) // 2


fib_40_time = timeit.timeit("fibonacci(40)", number=1, globals=globals())
print(f'Fibonacci 40 time is: {fib_40_time}')

for i in x:
    fib_time.append(timeit.timeit(f'fibonacci({i})', number=1, globals=globals()))
    fib_with_lucas_time.append(timeit.timeit(f'fib_with_lucas({i})', number=1, globals=globals()))

fig = plt.figure()

plt.plot(x, fib_time, color="red", label='Fib')
plt.plot(x, fib_with_lucas_time, color="orange", label='Fib with Lucas')

plt.ylabel("Time")
plt.xlabel("Elements")
plt.legend()

plt.show()
