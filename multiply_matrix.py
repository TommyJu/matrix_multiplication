"""
Tommy Ju
A01347715
"""
from prettytable import PrettyTable
from prettytable import SINGLE_BORDER
from prettytable import FRAME


def multiply_matrix(first_matrix: list, second_matrix: list) -> list:
    """
    Correctly multiplies the matrices

    :param first_matrix: a list representing a matrix
    :param second_matrix: a list representing a matrix
    :precondition: the number of columns of the first matrix must be equal to the number of rows of the second
    :postcondition: correctly determines the product of the  matrices
    :return: a list representing the solution matrix

    >>> multiply_matrix([[1, 2, 3], [4, 5, 6]], [[1], [1], [2]])
    [[9], [21]]
    """

    list_of_columns = covert_columns_to_rows(second_matrix)

    answer = []
    for matrix_row in first_matrix:
        # Multiply the row value with the column value at the corresponding index
        row_result = []
        for matrix_column in list_of_columns:
            row_value = multiply_and_sum_row_and_column(matrix_row, matrix_column)
            row_result.append(row_value)
        answer.append(row_result)

    return answer


def covert_columns_to_rows(matrix):
    """

    :param matrix:
    :return:

    >>> covert_columns_to_rows([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    """
    # Convert each column in the second matrix to a row in a list
    list_of_columns = []
    second_matrix_row_length = len(matrix[0])

    for column_position in range(second_matrix_row_length):
        column = [row[column_position] for row in matrix]
        list_of_columns.append(column)

    return list_of_columns


def multiply_and_sum_row_and_column(row, column):
    """

    :param row:
    :param column:
    :return:

    >>> multiply_and_sum_row_and_column([1, 2], [2, 3])
    8
    """
    terms_of_products = [row_value * column_value for row_value, column_value in zip(row, column)]
    return sum(terms_of_products)


def first_matrix_input() -> list:
    """
    Retrieve a valid matrix from the user

    :precondition: a matrix must be non-empty
    :precondition: a matrix must not have any missing values
    :postcondition: retrieves a valid matrix for multiplication

    :return: a list representing the matrix
    """
    matrix = []
    row_number = 1
    number_of_columns = None
    while True:
        print("First Matrix:")
        print(create_matrix_table(matrix))
        row_input = input(f"Input the value(s) of row {row_number} for the first matrix.\n"
                          f"Type 'next' to continue to the next matrix.\n").strip()
        # Prevent an empty matrix
        if row_input == "next" and not matrix or row_input == "":
            print(f"You must have a non-empty matrix or row value\n")
            continue

        # Move onto the next matrix
        if row_input == "next":
            return matrix

        row_values = row_input.split(" ")

        # Convert each row value from string to integer
        try:
            for column, value in enumerate(row_values):
                int(row_values[column])
        except ValueError:
            print(f"You must enter an integer for each row value or type 'next'.\n")
            continue

        # Use the first valid input to determine the number of columns the matrix has
        if not matrix:
            number_of_columns = len(row_values)

        # Ensure that there are no missing column entries for each row on valid input
        if len(row_values) != number_of_columns:
            print(f"You must enter a row with {number_of_columns} columns.\n")
            continue

        matrix.append(row_values)
        row_number += 1


def second_matrix_input(first_matrix_column_count: int) -> list:
    """
    Retrieve the second valid matrix from the user

    :param first_matrix_column_count: an integer representing the number of columns of the first matrix
    :precondition: a matrix must be non-empty
    :precondition: a matrix must not have any missing values
    :precondition: the number of rows of the second matrix must equal the number of columns of the first
    :postcondition: retrieves a valid matrix for multiplication

    :return: a list representing the matrix
    """
    matrix = []
    row_number = 1
    number_of_columns = None
    while True:
        print("Second Matrix:")
        print(create_matrix_table(matrix))
        row_values = input(f"Input the value(s) of row {row_number} for the second matrix.\n").strip().split(" ")

        # Convert each row value from string to integer
        try:
            for column, value in enumerate(row_values):
                int(row_values[column])
        except ValueError:
            print(f"You must enter an integer for each row value.\n")
            continue

        # Use the first valid input to determine the number of columns the matrix has
        if not matrix:
            number_of_columns = len(row_values)

        # Ensure that there are no missing column entries for each row on valid input
        if len(row_values) != number_of_columns:
            print(f"You must enter a row with {number_of_columns} columns.\n")
            continue

        matrix.append(row_values)

        # This condition must be true for us to correctly multiply 2 matrices
        if row_number == first_matrix_column_count:
            return matrix

        row_number += 1


def create_matrix_table(matrix: list):
    """
    Converts the matrix into an ASCII table

    :param matrix: a list of lists representing each row in a matrix
    :precondition: matrix must be non-empty
    :precondition: the matrix must be a nested list
    :postcondtion: a string representing the matrix is a table
    """
    table = PrettyTable()
    table.header = False
    table.set_style(SINGLE_BORDER)
    table.vrules = FRAME
    table.add_rows(matrix)
    return table


def main():
    sample_matrix = [[1, 2], [3, 4]]
    sample_table = create_matrix_table(sample_matrix)
    # print(first_matrix_input())
    print(multiply_matrix([[1, 2, 3], [4, 5, 6]], [[1], [1], [2]]))


if __name__ == "__main__":
    main()
