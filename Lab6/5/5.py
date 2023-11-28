import numpy as np

def seqLen(word1, word2):

    seqLenMatr = np.zeros((len(word1)+1, len(word2)+1), dtype='int')

    word_a = list(word1)
    word_b = list(word2)

    for i in range(1, np.shape(seqLenMatr)[0]):
        for j in range(1, np.shape(seqLenMatr)[1]):
            if word_a[i-1] == word_b[j-1]:
                seqLenMatr[i][j] = seqLenMatr[i-1][j-1] + 1
            else:
                seqLenMatr[i][j] = np.max((seqLenMatr[i-1][j], seqLenMatr[i][j-1]), axis=0)

    return np.max(seqLenMatr)


userString = input("Введите строку: ")
sim = []
count = int(input("Введите количество похожих слов: "))

print("Введите похожие слова:")
for i in range(count):
    sim.append(input())

seqLenDicts = [{'word': simW, 'seqLen': seqLen(userString, simW)} for simW in sim]

sortedLengths = sorted(seqLenDicts, key=lambda d: d['seqLen'], reverse=True)

print(sortedLengths[0])

