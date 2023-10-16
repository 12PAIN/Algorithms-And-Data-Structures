import random
import timeit as timeit
import matplotlib.pyplot as plt

from lists.Stack import Stack
from lists.Queue import Queue
from lists.Deque import Deque

x = [i for i in range(10, 1001, 10)]

dqTime = []
quTime = []
stckTime = []

dqTime_rem = []
quTime_rem = []
stckTime_rem = []


def add(struct):

    item = random.random()

    if isinstance(struct, Deque):
        struct.addFront(item)
    elif isinstance(struct, Stack):
        struct.push(item)
    elif isinstance(struct, Queue):
        struct.enqueue(item)


def deleteItem(struct):
    if isinstance(struct, Deque):
        struct.removeFront()
    elif isinstance(struct, Stack):
        struct.pop()
    elif isinstance(struct, Queue):
        struct.dequeue()


for i in x:
    dq = Deque()
    qu = Queue()
    stck = Stack()

    dqTime.append(timeit.timeit("add(dq)", number=i * 3, globals=globals()))
    quTime.append(timeit.timeit("add(qu)", number=i * 3, globals=globals()))
    stckTime.append(timeit.timeit("add(stck)", number=i * 3, globals=globals()))

    dqTime_rem.append(timeit.timeit("deleteItem(dq)", number=i * 3, globals=globals()))
    quTime_rem.append(timeit.timeit("deleteItem(qu)", number=i * 3, globals=globals()))
    stckTime_rem.append(timeit.timeit("deleteItem(stck)", number=i * 3, globals=globals()))

    # print(dqTime)
    # print(quTime)
    # print(stckTime)
    # print(dqTime_rem)
    # print(quTime_rem)
    # print(stckTime_rem)

fig = plt.figure()

plt.plot(x, dqTime, color="blue", label='Deque, Insert')
plt.plot(x, quTime, color="red", label='Queue, Insert')
plt.plot(x, stckTime, color="green", label='Stack, Insert')

plt.plot(x, dqTime_rem, color="cyan", label='Deque, Deletion')
plt.plot(x, quTime_rem, color="orange", label='Queue, Deletion')
plt.plot(x, stckTime_rem, color="yellow", label='Stack, Deletion')

plt.ylabel("Time")
plt.xlabel("Elements *3")
plt.legend()

plt.show()
