from Struct.HashTableChain import HashTable

H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"

print(H.slots)
print(H.data)
print(len(H))
print(20 in H)

print(H[20])

print(H[17])
H[20] = 'duck'
print(H[20])
print(H[99])

del H[54]
del H[26]
del H[93]
del H[17]
del H[77]
del H[31]
del H[44]

print(H.loadfactor())
print(H.slots)
print(H.data)
