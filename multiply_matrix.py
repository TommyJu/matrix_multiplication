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
    """
    pass


def first_matrix_input() -> list:
    """
    Retrieve a valid matrix from the user

    :precondition: a matrix must be non-empty
    :precondition: a matrix must not have any missing values
    :postcondition: retrieves a valid matrix for multiplication

    :return: a list representing the matrix
    """



def second_matrix_input(first_matrix: list) -> list:
    """
    Retrieve the second valid matrix from the user

    :precondition: a matrix must be non-empty
    :precondition: a matrix must not have any missing values
    :precondition: the number of rows of the second matrix must equal the number of columns of the first
    :postcondition: retrieves a valid matrix for multiplication

    :return: a list representing the matrix
    """
    pass


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


if __name__ == "__main__":
    main()
