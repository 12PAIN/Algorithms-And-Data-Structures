import numpy as np


def putToFirstAvailableBoxAlgorithm(items):
    boxesList = [[]]

    for i in range(0, len(items)):

        currentItem = items[i]

        for i in range(0, len(boxesList)):
            boxWeight = sum(boxesList[i])

            if 1.0 - boxWeight >= currentItem:
                boxesList[i].append(currentItem)
                break
            elif i != len(boxesList) - 1:
                continue
            else:
                boxesList.append([currentItem])

    return boxesList


def putToMostFitBoxAlgorithm(items):
    boxesList = [[]]

    for i in range(0, len(items)):

        currentItem = items[i]
        remainingSpaceAfterPut = [0] * len(boxesList)

        for i in range(0, len(boxesList)):
            boxWeight = sum(boxesList[i])

            remainingSpaceAfterPut[i] = 1.0 - (boxWeight + currentItem)

        remainingSpaceAfterPut = [i if i >= 0 else 1000 for i in remainingSpaceAfterPut]

        min_value = min(remainingSpaceAfterPut)
        min_idx = remainingSpaceAfterPut.index(min_value)

        if min_value == 1000:
            min_idx = len(boxesList)
            boxesList.append([])

        boxesList[min_idx].append(currentItem)

    return boxesList


def putToNextFitBoxAlgorithm(items):
    boxesList = [[]]

    currentBox = 0
    for i in range(0, len(items)):
        currentItem = items[i]

        if sum(boxesList[currentBox]) + currentItem > 1.0:
            boxesList.append([])
            currentBox += 1

        boxesList[currentBox].append(currentItem)

    return boxesList


def putToMinFitBoxAlgorithm(items):
    boxesList = [[]]

    for i in range(0, len(items)):

        currentItem = items[i]
        remainingSpaceAfterPut = [0] * len(boxesList)

        for i in range(0, len(boxesList)):
            boxWeight = sum(boxesList[i])

            remainingSpaceAfterPut[i] = 1.0 - (boxWeight + currentItem)

        remainingSpaceAfterPut = [i if i >= 0 else -1000 for i in remainingSpaceAfterPut]

        max_value = max(remainingSpaceAfterPut)
        max_idx = remainingSpaceAfterPut.index(max_value)

        if max_value == -1000:
            max_idx = len(boxesList)
            boxesList.append([])

        boxesList[max_idx].append(currentItem)

    return boxesList


for size in (50, 100, 200, 500):
    items = list(np.random.uniform(0.1, 1.0, size))

    availableAlgoBoxes = putToFirstAvailableBoxAlgorithm(items)
    mostFit = putToMostFitBoxAlgorithm(items)
    nextFit = putToNextFitBoxAlgorithm(items)
    minFit = putToMinFitBoxAlgorithm(items)

    print(f'{"Count:" + str(len(items)):=^30}')
    print(f'{"First Available:" + str(len(availableAlgoBoxes)): <30}')
    print(f'{"Most Fit:" + str(len(mostFit)): <30}')
    print(f'{"Next Fit:" + str(len(nextFit)): <30}')
    print(f'{"Min Fit:" + str(len(minFit)): <30}')
