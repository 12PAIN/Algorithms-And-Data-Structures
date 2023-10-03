import numpy as np

sudoku = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]
]

def checkrow(arr, x, y, n):
    fitsFlag = True
    row = arr[x]

    if n in row:
        fitsFlag = False

    return fitsFlag


def checkcol(arr, x, y, n):
    fitsFlag = True

    col = []
    for i in range (0, len(arr) - 1):
        col.append(arr[i][y])

    if n in col:
        fitsFlag = False

    return fitsFlag

def checksquare(arr, x, y, n):
    fitsFlag = True

    square = []

    arr_cpy_np = np.array(arr)

    sq_idx_x = 0 if x <= 1 else 2
    sq_idx_y = 0 if y <= 1 else 2

    sq_matr = arr_cpy_np[sq_idx_x:sq_idx_x+2, sq_idx_y:sq_idx_y+2]

    if n in sq_matr:
        fitsFlag = False

    return fitsFlag


def possible(arr, x, y, n):
    return checkrow(arr, x, y, n) and checkcol(arr, x, y, n) and checksquare(arr, x, y, n)

def solve(arr):
    # Список arr содержит 16 ячеек, 4 строки, 4 столбца. В цикле
    # перебираем каждую ячейку
    for x in range(4):
        for y in range(4):
            # И проверяем, пуста ли она
            if arr[x][y] == 0:
                # Если данная ячейка пуста, пробуем поставить в неё числа
                # от 1 до 4. Число считается подходящим, когда функция
                # possible(arr, x, y, n) возвращает True.
                for n in range(1, 5):
                    # Если подходящее число найдено
                    if possible(arr, x, y, n):
                        # то записываем его в список arr
                        arr[x][y] = n
                        # и вызываем функцию solve(arr) ещё раз
                        # этот вызов функции solve() отличается от предыдущего тем,
                        # что в списке arr стало на одну заполненную ячейку больше.
                        ## Если число n было выбрано удачно, то последующие вызовы solve(arr)
                        # приведут к решению, если выбранное число n впоследствии привело в тупик,
                        # значит ему не место в этой ячейке и нужно вернуть ячейке значение '0'.
                        solve(arr)
                        # Это строчка выполняется когда цепочка вызовов
                        # solve(arr) достигает "дна" (см. Deep First Recursion) и при этом
                        # решение до сих пор не найдено.
                        ## Достигает "дна" означает, что внутри предыдущего вызова
                        # solve(arr) сработал return вместо очередного вызова функции
                        # solve(arr)
                        ## А раз решение не найдено, значит n, которое мы добавили
                        # в arr две строки назад (arr[x][y] = n) привело в тупик -
                        # отменяем его.
                        arr[x][y] = 0
                # Здесь мы можем оказаться только в случае arr[x][y] == 0,
                # другими словами, если в списке arr остались пустые ячейки.
                # Когда пустых ячейк не останется, мы не попадём в этот блок if
                # и соответственно данный return не сработает.
                return
    # До этой строки дойдём только когда список arr заполнен целиком - решение найдено,
    # все остальные вызовы функции solve() будут заканчиваться на предыдущей строке
    # с "return"
    print(np.matrix(arr))

solve(sudoku)
