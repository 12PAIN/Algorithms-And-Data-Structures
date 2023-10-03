# Напишите рекурсивную функцию recursive_two(some_list), которая возвращает
# кортеж из двух значений – наибольший элемент списка some_list и второй наибольший его
# элемент.
import random
from cmath import inf


def recursive_max(some_list):
    print(len(some_list))
    if len(some_list) == 1:
        return some_list

    idx = int(len(some_list) / 2)
    maxElement = recursive_max(some_list[0:idx])

    maxTest2 = recursive_max(some_list[idx:])

    maxElement = maxElement if maxElement > maxTest2 else maxTest2

    return maxElement


def recursive_two(some_list):
    # print(len(some_list))
    if len(some_list) == 2:
        return (some_list[0], some_list[1]) if some_list[0] > some_list[1] else (some_list[1], some_list[0])

    if len(some_list) == 1:
        return some_list[0], -inf

    idx = int(len(some_list) / 2)
    maxElement, maxElement2 = recursive_two(some_list[0:idx])

    maxElementTest, maxElementTest2 = recursive_two(some_list[idx:])

    if maxElementTest > maxElement:
        maxElement2 = maxElement if maxElement > maxElementTest2 else maxElementTest2
        maxElement = maxElementTest
    elif maxElementTest2 > maxElement2 or maxElementTest > maxElement2:
        maxElement2 = maxElementTest2 if maxElementTest2 > maxElementTest else maxElementTest

    return maxElement, maxElement2


values = [1, 2, 1300, 15, 3, 4, 5, 100, 6, 10000, 7, 8, 9, 10, 11, 12, 13, 1500]

print(recursive_two(values))
