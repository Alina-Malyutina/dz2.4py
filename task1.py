matrix_start = [[1, 2, 3], [5, 8, 7], [9, 2, 4]]
result_finish = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def Transporte(matrix, result_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[j][i] = matrix[i][j]
    return result_matrix


print(Transporte(matrix_start, result_finish))
