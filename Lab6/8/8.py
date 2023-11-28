import random


def greedy_find_sum(needed, billsAndCounts):
    to_pay_bills = {bill: 0 for bill in list(billsAndCounts.keys())[::-1]}
    currentRemains = needed

    for bill in to_pay_bills.keys():
        countBills = currentRemains // bill
        if countBills > billsAndCounts[bill]:
            countBills = billsAndCounts[bill]


        currentRemains -= countBills * bill
        to_pay_bills[bill] = countBills

    if currentRemains != 0:
        raise ValueError

    return to_pay_bills


# clientsCountList = [3, 10, 50, 100]
clientsCountList = [random.randint(3, 10)]

for clientsCount in clientsCountList:

    print(f'Новый день! Теперь клиентов: {clientsCount}')
    print()

    clients = []

    for client in range(0, clientsCount):
        clients.append(random.randint(200, 1001))

    atmBills = {
        1: random.randint(clientsCount, 3*clientsCount+1),
        3: random.randint(clientsCount, 3*clientsCount+1),
        4: random.randint(clientsCount, 3*clientsCount+1),
        10: random.randint(clientsCount, 3*clientsCount+1),
        50: random.randint(clientsCount, 3*clientsCount+1),
        100: random.randint(clientsCount, 3*clientsCount+1)
    }

    print('В банкомате:')
    for bill in atmBills.keys():
        print(f'{bill}:{atmBills[bill]}')
    print()

    for clientSum in clients:
        try:
            clientBills = greedy_find_sum(clientSum, atmBills)
            count = 0
            for bill in clientBills.keys():
                atmBills[bill] -= clientBills[bill]
                count += clientBills[bill]
            print(f'Выдано {clientSum} количеством купюр и монет {count}')

        except ValueError as ve:
            print(f'Не получилось выдать {clientSum} клиенту')

    print()
