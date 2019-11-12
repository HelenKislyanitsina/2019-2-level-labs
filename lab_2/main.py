"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_columns: int) -> list:
    if not isinstance(num_rows, int) or not isinstance(num_columns, int):
        return []
    matrix = []
    for i in range(num_rows):
        matrix.append([0] * num_columns)
        i += 1
    return matrix


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    matrix = list(edit_matrix)
    if not matrix:
        return matrix
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return matrix
    if not matrix[0]:
        return matrix
    for i in range(1, len(matrix)):
        matrix[i][0] = matrix[i - 1][0] + remove_weight
    for j in range(1, len(matrix[0])):
        matrix[0][j] = matrix[0][j - 1] + add_weight
    return matrix


def minimum_value(numbers: tuple) -> int:
    values = list(numbers)
    minimum = min(values)
    return minimum


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    matrix = list(edit_matrix)
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int) \
            or not isinstance(original_word, str) or not isinstance(target_word, str):
        return matrix
    for i in range(1, len(matrix)):
        for k in range(1, len(matrix[i])):
            add = matrix[i][k - 1] + add_weight
            remove = matrix[i - 1][k] + remove_weight
            if original_word[i - 1] == target_word[k - 1]:
                substitute = matrix[i - 1][k - 1]
            else:
                substitute = matrix[i - 1][k - 1] + substitute_weight
            matrix[i][k] = minimum_value((add, remove, substitute))
    return matrix


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    if not isinstance(original_word, str) or not isinstance(target_word, str) or not isinstance(add_weight, int) or not\
            isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return -1
    first_step = tuple(generate_edit_matrix(len(original_word) + 1, len(target_word) + 1))
    second_step = tuple(initialize_edit_matrix(first_step, add_weight, remove_weight))
    third_step = fill_edit_matrix(second_step, add_weight, remove_weight, substitute_weight, original_word, target_word)
    final = third_step[-1][-1]
    return final


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:
    file = open(path_to_file, 'w')
    matrix = ''
    for string in edit_matrix:
        matrix += str(string)
        matrix += '\n'
    matrix = matrix.replace('[', '')
    matrix = matrix.replace(']', '')
    matrix = matrix.replace(' ', '')
    file.write(matrix)


def load_from_csv(path_to_file: str) -> list:
    file = open(path_to_file, 'r')
    matrix = []
    final_matrix = []
    for line in file:
        for i in line:
            if i not in (',', '\n'):
                matrix.append(i)
        final_matrix.append(matrix)
        matrix = []
    print(final_matrix)
    return final_matrix
