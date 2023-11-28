import itertools
import string
import timeit
import matplotlib.pyplot as plt
import numpy as np
import random


###
### Полный перебор займет O(2^n)
###
def full_search(maxWeight, items):
    final_weight = 0
    final_cost = 0
    final_items = []

    for i in range(1, len(items) + 1):
        for _ in itertools.combinations(items, i):
            weight = sum(item['weight'] for item in _)
            cost = sum(item['cost'] for item in _)

            if cost > final_cost and weight <= maxWeight:
                final_cost = cost
                final_weight = weight
                final_items = _

    return final_items, final_weight, final_cost


###
### Для жаднго алгоритма O(n)
###
def greedy_search(maxWeight, items):

    itemsSorted = list(items)

    itemsSorted = sorted(itemsSorted, key=lambda d: d['cost'], reverse=True)

    currentWeight = 0
    currentCost = 0
    items = []
    for item in itemsSorted:

        if currentWeight + item['weight'] <= maxWeight:
            items.append(item)
            currentWeight += item['weight']
            currentCost += item['cost']
        else:
            continue

    return items, currentWeight, currentCost

###
### Для динамического алгоритма O(n*k) - где n - количество вещей, k - размерность рюкзака
###
def dynamic_search(maxWeight, items):
    n = len(items)
    table = [[0] * (maxWeight + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, maxWeight + 1):
            weight = items[i - 1]['weight']
            cost = items[i - 1]['cost']
            if weight > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - weight] + cost)

    res_items = []
    res_weight = 0
    res_cost = 0
    i, j = n, maxWeight
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            res_items.append(items[i - 1]['title'])
            res_weight += items[i - 1]['weight']
            res_cost += items[i - 1]['cost']
            j -= items[i - 1]['weight']
        i -= 1

    return res_items[::-1], res_weight, res_cost


# maxWeight = float(input('Введите максимальный вес->'))
# n = int(input('Введите количество предметов->'))
# print()
#
#
# itemsList = []
# for i in range(0, n):
#     itemName = input('Введите имя предмета->')
#     itemWeight = float(input('Введите вес предмета->'))
#     itemCost = float(input('Введите цену предмета->'))
#
#     print()
#     itemsList.append({
#         'name': itemName,
#         'cost': itemCost,
#         'weight': itemWeight
#     })
#
#
# final_items_full, final_weight_full, final_cost_full = full_search(maxWeight=maxWeight, items=itemsList)
# final_items_greedy, final_weight_greedy, final_cost_greedy = greedy_search(maxWeight=maxWeight, items=itemsList)
# final_items_dynamic, final_weight_dynamic, final_cost_dynamic = dynamic_search(maxWeight=maxWeight, items=itemsList)
#
# print(final_items_full)
# print(final_weight_full, final_cost_full)
#
# print()
#
# print(final_items_greedy)
# print(final_weight_greedy, final_cost_greedy)
#
# print()
#
# print(final_items_dynamic)
# print(final_weight_dynamic, final_cost_dynamic)



plt_x = []
plt_search = []
plt_greedy = []
plt_dynamic = []
time_search = timeit.Timer('full_search(v, items)', globals=globals())
time_greedy = timeit.Timer('greedy_search(v, items)', globals=globals())
time_dynamic = timeit.Timer('dynamic_search(v, items)', globals=globals())

for i in range(1, 10):
    plt_x.append(i)
    v = random.randint(1, 100)
    items = [{'title': ''.join(random.choice(string.ascii_lowercase) for m in range(v)),
              'weight': random.randint(1, 10),
              'cost': random.randint(1, 20)} for j in range(i)]

    time1 = time_search.timeit(number=3)
    plt_search.append(time1)

    time2 = time_greedy.timeit(number=3)
    plt_greedy.append(time2)

    time3 = time_dynamic.timeit(number=3)
    plt_dynamic.append(time3)

print(plt_greedy)

plt.plot(plt_x, plt_search, label='Full Search')
plt.plot(plt_x, plt_greedy, label='Greedy algorithm')
plt.plot(plt_x, plt_dynamic, label='Dynamic programming')
plt.xlabel('Items length')
plt.ylabel('Runtime * 3')
plt.legend()
plt.show()