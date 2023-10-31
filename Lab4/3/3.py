from Struct.HashTableWithStrings import HashTable

H = HashTable()
H["54"] = "cat"
H["dog"] = "dog"

print(H.slots)
print(H.data)
print(len(H))

print(H["54"])
print(H["dog"])
