# Functions go here
def question_type(question, error):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or "y":
            response = "yes"
            return response
        elif response == "":
            response = "no"
            return response
        else:
            print(error)


# Main routine
question_type_error = ("error plaese enter yes or blank")

print("Which questions would you like \n"
"Yes for those questions blank to skip.")
addition = question_type("Addition: ", question_type_error)
subtraction = question_type("Subtraction: ", question_type_error)
multiply = question_type("Multiplication: ", question_type_error)
division = question_type("Division: ", question_type_error)
