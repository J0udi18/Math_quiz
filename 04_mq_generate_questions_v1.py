# Import random
from os import pardir
import random

# functions
# yes no checker checks for yes or no inputs
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> Please say yes or no")
            print()


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, low=None, high=None):

    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if low is not None and high is not None:
                if low < response < high:
                    return response
                else:
                    print(error)
                    print()
                    continue

            elif low is not None:
                if response > low:
                    return response
                else:
                    print(error)
                    print()
                    continue

            else:
                return response

        except ValueError:
            print(error)
            print()


# main routine goes here
# ask user for which type of questions
print("Which questions would you like \n"
"Yes for those questions blank to skip.")
print()
addition = yes_no("Addition: ")
subtraction = yes_no("Subtraction: ")
multiply = yes_no("Multiplication: ")
division = yes_no("Division: ")
print()

# ask uesr for number of questions
num_questions_error = "<error> enter an interger"
num_questions = num_check("How many questions? ", num_questions_error, int, 0)
print()


# Generate questions 
while num_questions > 0:
 
    int_i = random.randint(1, 100)
    int_ii = random.randint(1, 100)

    question = int(input("{} + {} = ".format(int_i, int_ii)))
    ans = int_i + int_ii

    if question == ans:
        print("You got it right")
    else:
        print("You got it wrong")
    print()

    num_questions -= 1
