from typing import List


def add_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    result = []
    for i in range(len(matrix1)):
        vector = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))]
        result.append(vector)
    return result


def subtract_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    pass


def devise_matrices(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    pass


def invert_matrix(matrix: List[List[int]]) -> List[List[int]]:
    pass


def compute_determinant(matrix: List[List[int]]) -> List[List[int]]:
    pass


def raise_to_power(matrix: List[List[int]], power: int) -> List[List[int]]:
    pass
