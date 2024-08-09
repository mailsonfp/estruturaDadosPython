def solution(array):
    exits_repetead_number = False
    array.sort()

    point_one = 0
    point_two = 1

    for i in range(len(array)):
        print(f'point_one: {point_one}')
        print(f'point_two: {point_two}')
        print(f'arr[point_one]: {array[point_one]}')
        print(f'arr[point_two]: {array[point_two]}')
        if array[point_one] == array[point_two]:
            return True

        point_one += 1
        point_two += 1

        print(f'point_one: {point_one}')
        print(f'point_two: {point_two}')

        if point_one == len(array) - 1:
            break

        print('-' * 20)

    return False

def solution_mat(mat):
    quantity_lines = len(mat)
    quantity_columns = len(mat[0])

    print(f'quantity_lines: {quantity_lines}')
    print(f'quantity_columns: {quantity_columns}')

    matrix_return = [0] * quantity_lines

    point_line = 0
    point_column = quantity_columns - 1

    print(f'point_column: {point_column}')

    for i in range(quantity_lines):
        print(f'i: {i}')
        line = []
        for j in range(quantity_columns):
            print(f'j: {j}')
            print(f'point_line: {point_line}')
            print(f'point_column: {point_column}')

            print(f'mat[point_line][point_column]: {mat[point_line][point_column]}')
            line.append(mat[point_line][point_column])

            point_line += 1

        matrix_return[i] = line

        point_column -= 1
        point_line = 0

        print('-' * 20)

    return matrix_return


def solution_word(mat, word):
    exist_word = False
    count_letter = 0
    length_word = len(word)

    quantity_lines = len(mat)
    quantity_columns = len(mat[0])

    for line in range(quantity_lines):
        print(f'Line: {line}' + ('-' * 20))

        exist_word = True
        for column in range(quantity_columns):
            print(f'Column: {column}' + ('-' * 20))
            for letter in word:
                print(f'mat[line][column]: {mat[line][column]}')
                print(f'letter: {letter}')
                if mat[line][column] == letter:
                    count_letter += 1
                    word = word.replace(letter, '')
                    print(f'word: {word}')
                    break

        if count_letter == length_word:
            exist_word = True
            break

    return exist_word


if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(solution_mat(mat))
    # mat = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    # ]
    #
    # word = "ABBC"
    #
    # print(solution_word(mat, word))
