"""
 1. This program can convert each element in the array into its binary representation.
"""
import numpy as np
def convert_to_binary(number):
    """
    1. This function converts the normal decimal values to the binary values. Here \
    2. The loop takes a number and convert it into the binary by appending it to the string \
    3. After the division. The result is returned as a string reversed.
    """
    str_num = ""
    while number:
        str_num += str(number % 2)
        number = int(number / 2)
    return str_num[::-1]



output_array = []


def main():
    """
    Function for taking input and calling helper function to convert the 
    number into binary
    """

    elements = input("Please input the number of element to convert in Binary")   
    binary_list = []
    #This loop will take input of the list element.
    for i in range(0, int(elements)):
        num = input("Enter decimal number :")
        binary_list.append(num)
    # Converting the list to numpy array.
    input_array = np.array(binary_list)
    # Calling the function convert to binary for conversion of number and appending it back to 
    #list
    for i in input_array:
        output_array.append((convert_to_binary(int(i))))

main()
print(output_array)
