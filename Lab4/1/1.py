from Struct.HashTableProbe import HashTable

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
print('bird' in H)

print(H[20])

print(H[17])
H[20] = 'duck'
print(H[20])
print(H[99])

del H['duck']
del H["pig"]
del H["goat"]
del H["bird"]
del H["tiger"]
del H["cat"]
del H["cow"]
print(H.loadfactor())
print(H.slots)
print(H.data)
