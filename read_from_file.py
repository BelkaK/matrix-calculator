from typing import List


def read_matrix_from_file(directory: str, separating_char: str) -> List[List[float]]:

    read_matrix = []

    try:
        file_holder = open(directory, 'r')
        for line in file_holder:
            line_of_numbers = line.strip('\n')
            read_matrix.append([float(number) for number in line_of_numbers.split(separating_char)])
        file_holder.close()
    except (FileExistsError, FileNotFoundError):
        pass
    return read_matrix
