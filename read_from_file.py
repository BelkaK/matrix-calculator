from typing import List


def read_matrix_from_file() -> List[List[float]]:

    read_matrix = []
    directory = input('Podaj scieżkę:')
    separating_char = input('Podaj symbol rozdzielający liczby macierzy:')

    with open(directory, 'r') as file_holder:
        for line in file_holder:
            line_of_numbers = line.strip('\n')
            read_matrix.append([float(number) for number in line_of_numbers.split(separating_char)])
    return read_matrix
