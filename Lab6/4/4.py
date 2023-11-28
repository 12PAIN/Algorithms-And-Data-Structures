import numpy as np

def substrLen(word1, word2):

    substrMatr = np.zeros((len(word1)+1, len(word2)+1), dtype='int')

    word_a = list(word1)
    word_b = list(word2)

    for i in range(1, np.shape(substrMatr)[0]):
        for j in range(1, np.shape(substrMatr)[1]):
            if word_a[i-1] == word_b[j-1]:
                substrMatr[i][j] = substrMatr[i-1][j-1] + 1
            else:
                substrMatr[i][j] = 0

    return np.max(substrMatr)


userString = input("Введите строку: ")
sim = []
count = int(input("Введите количество похожих слов: "))

print("Введите похожие слова:")
for i in range(count):
    sim.append(input())

substrLengthsDict = [{'word': simW, 'substrLen': substrLen(userString, simW)} for simW in sim]

sortedLengths = sorted(substrLengthsDict, key=lambda d: d['substrLen'], reverse=True)

print(sortedLengths[0])

