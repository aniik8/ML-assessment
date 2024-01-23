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
np_matrix = np.array([[5, 3, 1], [9, 25, 1], [4, 7, 10]])
column = 0

def student_marks(np_array, columns):
    """
    The argsort function in NumPy returns an array of indices that would 
    sort an array along a specified axis
    """
    sorted_arr = np_matrix[np_array[:, columns].argsort()]

    return sorted_arr


def main():
    """Function for taking input and calling helper function student_marks"""
    # Number of test cases
    num_test_cases = int(input("Number of test cases: "))

    for _ in range(num_test_cases):
        # Number of rows and column to be sorted
        rows, sort_column = map(int, input().split())

        # Input matrix as a list, map is used because input taken in is a string so converting to int
        input_matrix = [list(map(int, input().split())) for _ in range(rows)]

        # Sort the matrix based on the specified column
        result_matrix = student_marks(input_matrix, sort_column)

        # Output
        print(result_matrix)

print(student_marks(np_matrix, column))
