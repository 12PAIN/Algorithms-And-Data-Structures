import numpy as np

arr1 = np.array(['Python', 'PHP'])
arr2 = np.array(['Java', 'C ++'])

arr1 = np.char.add(arr1,  " ")
print(np.char.add(arr1,  arr2))