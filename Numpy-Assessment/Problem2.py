"""
You have access to every student’s marks in every quiz. The marks are stored in a matrix
where matrix[i][j] represents the marks of the ith student in the jth quiz.
The instructor wants you to sort the marks of students according to jth quiz in increasing
order
 so that he can evaluate the performance of students in that particular quiz.
Here, you have to create a python program using which the instructor 
can sort the data on
the basis of a given column(quiz). The program will return the 
matrix with the marks sorted in
jth quiz.
The dimension of the input matrix is mxn, the output is expected 
to be a 2d numpy matrix of
dimension mxn, but in the output the jth column must be arranged 
in the ascending order.
"""

import numpy as np

def sort_matrix(matrix, column):
    """
    The argsort function in NumPy returns an array of indices that would 
    sort an array along a specified axis
    """
    np_matrix = np.array(matrix)

    sorted_matrix = np_matrix[np_matrix[:, column].argsort()]

    return sorted_matrix

def main():
    """
    Function for taking input and calling helper function student_marks
    """
    # Number of test cases
    num_test_cases = int(input("Number of test cases: "))

    for _ in range(num_test_cases):
        rows, sort_column = map(int, input().split())

        input_matrix = []
        for _ in range(rows):
            row = list(map(int, input().split()))
            input_matrix.append(row)

        # Sort the matrix based on the specified column
        result_matrix = sort_matrix(input_matrix, sort_column)

        # Output the sorted matrix
        print(result_matrix)

main()