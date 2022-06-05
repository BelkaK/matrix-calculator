from typing import List


def add_matrices(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    result = []
    for i in range(len(matrix1)):
        vector = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))]
        result.append(vector)
    return result


def subtract_matrices(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    pass


def devise_matrices(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    pass


def invert_matrix(matrix: List[List[float]]) -> List[List[float]]:
    pass


def compute_determinant(matrix: List[List[float]]) -> List[List[float]]:
    pass


def raise_to_power(matrix: List[List[float]], power: float) -> List[List[float]]:
    pass
