import hashlib
import os
from Struct.HashTableWithStrings import HashTable


table = HashTable()

# Указываем путь к директории
directory = input()

# Получаем список файлов
files = os.listdir(directory)

for file in files:
    if os.path.isdir(f"{directory}/{file}"):
        continue

    with open(f"{directory}/{file}", 'rb', buffering=0) as f:

        fileHash = hashlib.file_digest(f, 'sha256').hexdigest()

        if table[fileHash] is not None:
            print(f"Duplicated file found -> \"{file}\" and \"{table[fileHash]}\"")
        else:
            table[fileHash] = file


