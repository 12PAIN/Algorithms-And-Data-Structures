import numpy as np

sudoku = np.array([
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
])

print(sudoku[2:4, 2:4])