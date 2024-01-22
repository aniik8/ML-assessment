"""Question 1 
1. Given a Numpy array of integers as an input to the function binary(), your task is to convert
each element in the array into its binary representation.
"""
import numpy as np
def convert_to_binary(number):
    """This function converts the normal decimal values to the binary values. Here \
    The loop takes a number and convert it into the binary by appending it to the string \
    After the division. The result is returned as a string reversed.
    """
    str_num = ""
    while number:
        str_num += str(number % 2)
        number = int(number / 2)
    return str_num[::-1]


input_Array1  = np.array([5, 10, 16, 32])
output_array = []
for i in input_Array1:
    output_array.append(convert_to_binary(i))

print(output_array)
