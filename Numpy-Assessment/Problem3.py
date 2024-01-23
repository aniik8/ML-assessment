"""
You are tasked to write a program that can find the number of times a student has accessed
a particular question
"""
import numpy as np
student_question = list([[]])
def accessed_question(number_students):
    """
    This function takes student question that he/she accessed and put them into the array.
    """
    for i in range(0, number_students):
        student_question.append([])
        print(f"Enter the questions of student {i+1}")
        for j in range(0, 11):
            question = int(input("Please enter the Question :"))
            if question > 10:
                print("Please enter a valid Question number")
                j -= 1
            else:
                student_question[i].append(question)
    return student_question


def main():
    """
    This function takes the input as number of students and Send them to the function for counting.
    Also displays the output 
    """
    number_students = int(input("Please enter the number of students?"))
    print(accessed_question(np.array(number_students)))

main()
