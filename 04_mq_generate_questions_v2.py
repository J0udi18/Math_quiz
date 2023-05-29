# Import 
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


# definition that generates questions randomly and will call this function 
def question(symbol):
    valid = False
    while not valid:
        # Generate random intergers
        int_i = random.randint(1, 100)
        int_ii = random.randint(1, 100)

        ans = eval(str(int_i) + symbol + str(int_ii))
        response = float(input("{} {} {} = ".format(int_i, symbol, int_ii)))

        if response == ans:
            print("You got it right")
            result = "correct"
            print()
            return result
        else:
            print("You got it wrong")
            result = "incorrect"
            print()
            return result


# checks what type of questions a user wants
def question_checker(question):
    valid = False
    while not valid:

        response = input(question).lower()
        # set list  of the type of questions
        ques_type_list = ["a", "s", "m", "d", ""]

        # Checks how long word is
        if response not in ques_type_list:
            print("error please first letter of math question eg: a for addition\n"
            "OR press <eneter> for all types of questions")
            continue
        else:
            return response


# main routine goes here
# reset variables
correct_questions = 0
incorrect_questions = 0
questions_list = []

# symbol list
symbol_list = ["+", "-", "*", "/"]

# ask user for which type of questions they would like
question_type = question_checker("Which type of questions would you like? ")
print(question_type)


# ask uesr for number of questions
num_questions_error = "<error> enter an interger"
num_questions = num_check("How many questions? ", num_questions_error, int, 0)
print()


# Generate questions
while num_questions > 0:
    # generates questions depending on what type you choose
    if question_type == "a":
        result = question("+")
    elif question_type == "s":
        result = question("-")
    elif question_type == "m":
        result = question("x")
    elif question_type == "d":
        result = question("/")
    else:
        result = question(random.choice(symbol_list))

    # Add result to a list and add number of correct and incorrect questions
    if result == "correct":
        correct_questions += 1
    else:
        incorrect_questions += 1
    questions_list.append("Question #1: {}".format(result))
    
    # number of questions left go down
    num_questions -= 1

print("Question answered correctly", correct_questions)
print("Question answered incorrectly", incorrect_questions)

