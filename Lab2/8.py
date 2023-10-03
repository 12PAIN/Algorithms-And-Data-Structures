sudoku = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

numbers_list = [1,2,3,4]

def count_zero(matrix):
    count = 0
    for i in matrix:
        for j in i:
            if j == 0:
                count += 1
    return count

def solve_sudoku(matrix):

    if count_zero(matrix) == 1:

