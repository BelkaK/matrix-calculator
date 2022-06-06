from typing import List


def subtract_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(matrix1)):
        vector = []
        for j in range(len(matrix1)):
            vector.append(matrix1[i][j] - matrix2[i][j])
        result.append(vector)
    return result


def add_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(matrix1)):
        vector = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))]
        result.append(vector)
    return result


def raise_to_power(matrix: List[List[int]], power: int) -> List[List[int]]:
    matrix_const = matrix[:]
    for n in range(0, (power - 1)):
        for i in range(len(matrix)):
            vector = []
            for j in range(len(matrix[i])):
                short_time_result = 0
                for k in range(len(matrix)):
                    short_time_result += matrix[i][k] * matrix_const[k][j]
                vector.append(short_time_result)
            matrix[i] = vector
    return matrix


def multiply_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(matrix1)):
        vector = []
        for j in range(len(matrix1[i])):
            short_time_result = 0
            for k in range(len(matrix1)):
                short_time_result += matrix1[i][k] * matrix2[k][j]
            vector.append(short_time_result)
        result.append(vector)
    return result


def multiply_matrix(matrix: List[List[int]], number: int) -> List[List[int]]:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] *= number
    return matrix


def divide_matrix(matrix: List[List[int]], number: int) -> List[List[float]]:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] *= 1/number
    return matrix


def compute_determinant(matrix: List[List[int]]) -> int:
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        result = 0
        for i in range(len(matrix)):
            minor = []
            for j in range(1, len(matrix)):
                minor.append(matrix[j][0:i]+matrix[j][i+1:len(matrix)+1])
            result += ((-1)**i)*matrix[0][i]*compute_determinant(minor)
        return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    result = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result


def invert_matrix(matrix: List[List[int]]) -> List[List[float]]:
    complement_matrix = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            minor = []
            for k in range(0, i):
                vector = []
                vector = (matrix[k][0:j]+matrix[k][j+1:])
                minor.append(vector)
            for k in range(i+1, len(matrix)):
                vector = []
                vector = (matrix[k][0:j]+matrix[k][j+1:])
                minor.append(vector)
            complement_matrix[i][j] = ((-1)**(i+j))*compute_determinant(minor)
    transposed_complement_matrix = transpose_matrix(complement_matrix)
    return divide_matrix(transposed_complement_matrix, compute_determinant(matrix))
# o tu w odwracaniu coś jest nie tak ale sie chyba zaraz zrzygam jakbym miał przy tym dzis siedziec, jutro dokoncze XD
