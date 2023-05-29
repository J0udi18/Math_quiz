# Functions
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



# Main routine

print("Which questions would you like \n"
"Yes for those questions blank to skip.")
print()
addition = yes_no("Addition: ")
subtraction = yes_no("Subtraction: ")
multiply = yes_no("Multiplication: ")
division = yes_no("Division: ")
