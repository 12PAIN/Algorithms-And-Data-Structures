import timeit as timeit
import matplotlib.pyplot as plt
import numpy as np
import random as rnd

x = [i for i in range(1000, 10001, 1000)]
fast_sorted = []
fast_random = []
fast_reversed = []

select_sorted = []
select_random = []
select_reversed = []


def myFastSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = rnd.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return myFastSort(l_nums) + e_nums + myFastSort(b_nums)


def mySelectSort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]


for i in x:
    arr_1 = [rnd.randint(-1000, 1000) for j in range(1, i)]
    arr_2 = [rnd.randint(-1000, 1000) for j in range(1, i)]
    fast_random.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    select_random.append(timeit.timeit("mySelectSort(arr_2)", number=1, globals=globals()))

    arr_1 = myFastSort(arr_1)
    mySelectSort(arr_2)

    fast_sorted.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    select_sorted.append(timeit.timeit("mySelectSort(arr_2)", number=1, globals=globals()))

    arr_1.sort(reverse=True)
    arr_2.sort(reverse=True)

    fast_reversed.append(timeit.timeit("myFastSort(arr_1)", number=1, globals=globals()))
    select_reversed.append(timeit.timeit("mySelectSort(arr_1)", number=1, globals=globals()))

fig = plt.figure()

plt.plot(x, fast_random, color="red", label='Fast, Random')
plt.plot(x, select_random, color="orange", label='Select, Random')

plt.plot(x, fast_sorted, color="blue", label='Fast, Sorted')
plt.plot(x, select_sorted, color="cyan", label='Select, Sorted')

plt.plot(x, fast_reversed, color="green", label='Fast, Reversed')
plt.plot(x, select_reversed, color="violet", label='Select, Reversed')

plt.ylabel("Time")
plt.xlabel("Elements")
plt.legend()

plt.show()
