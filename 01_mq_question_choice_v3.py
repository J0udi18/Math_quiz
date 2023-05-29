# Functions
def question_checker(question):
    valid = False
    while not valid:

        response = input(question).lower()
        # set list  of the type of questions
        ques_type_list = ["a", "s", "m", "d", ""]

        # Checks how long word is
        if response not in ques_type_list:
            print("<error> please first letter of math question eg: a for addition\n"
            "OR press <eneter> for all types of questions")
            print()
            continue
        else:
            return response


# Main routine
# Ask user for question type
question_type = question_checker("Which type of questions would you like? ")
print(question_type)