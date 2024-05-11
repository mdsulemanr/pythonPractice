def addition(matrix_1, matrix_2):

    rows_of_matrix1 = len(matrix_1)
    rows_of_matrix2 = len(matrix_2)
    if rows_of_matrix1 != rows_of_matrix2:
        return False

    for row in range(rows_of_matrix1):
        if len(matrix_1[row]) != len(matrix_2[row]):
            return False
    c = []
    i = 0
    while i < rows_of_matrix1:
        c.append([])
        j = 0
        while j < len(matrix_1[i]):
            c[i].append((matrix_1[i][j] + matrix_2[i][j]))
            j += 1
        i += 1
    return c


a = [[1, 2, 3],
     [2, 3, 4],
     [3, 4, 1]]
b = [[7, 2, 3],
     [2, 4, 5],
     [3, 2, 0]]

print(addition(a, b))

a = [[1, -5],
     [-1, 3],
     [0, 4]]
b = [[7, 2],
     [2, 4],
     [3, 2]]

print(addition(a, b))

a = [[2, 3, 4],
     [3, 4, 1]]
b = [[7, 2, 3],
     [3, 2, 0]]

print(addition(a, b))

a = [[1, 2],
     [2, 3],
     [3, 4]]
b = [[7, 2, 3],
     [2, 4, 5],
     [3, 2, 0]]

print(addition(a, b))

a = [[1, 2, 3],
     [2, 3, 4],
     [3, 4, 1]]
b = [[2, 4, 5],
     [3, 2, 0]]

print(addition(a, b))
