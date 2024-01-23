"""
This is a program that can find the number of times a student has accessed
a particular question.
"""
import numpy as np

def access_matrix(test_cases, matrix):
    """
    This function takes the matrix as an input along with test_cases and calculate the number of 
    times a particular question is accessed by a student.
    """
    result_matrices = []
    for i in range(test_cases):
        rows, columns = matrix[i].shape
        access_count_matrix = np.zeros((rows, 10), dtype=int)

        for row in range(rows):
            for col in range(columns):
                question_id = matrix[i][row, col]
                access_count_matrix[row, question_id - 1] += 1

        result_matrices.append(access_count_matrix)

    return result_matrices

# Input
test_case = int(input("Please enter the number of test cases"))
matrices = []

for _ in range(test_case):
    student = int(input("Please enter the number of students"))
    matrixs = np.array([list(map(int, input().split())) for _ in range(student)])
    matrices.append(matrixs)

# Calculate and print the result
result = access_matrix(test_case, matrices)
for j in range(test_case):
    print(result[j])
