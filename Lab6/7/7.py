import numpy as np

def greedy_find_sum(needed):
    bills = [1, 3, 4, 10, 50, 100]

    bills = bills[::-1]

    to_pay_bills = {bill: 0 for bill in bills}
    currentRemains = needed

    for bill in bills:
        countBills = currentRemains // bill
        currentRemains -= countBills * bill
        to_pay_bills[bill] = countBills

    return to_pay_bills


def dynamic_find_count(n):
    bills = [1, 3, 4, 10, 50, 100]
    table = [0 if i == 0 else float('inf') for i in range(n + 1)]
    for currentNeeded in range(1, n + 1):
        for bill in bills:
            if currentNeeded - bill >= 0:
                table[currentNeeded] = min(table[currentNeeded], table[currentNeeded - bill] + 1)
    return table[n]

### Пример входных данных, когда жадный алгоритм даёт неоптимальный ответ
sum = 6
print(f'Необходимая сумма - {sum}')
print(greedy_find_sum(sum))
print(dynamic_find_count(sum))



