# functions
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


# function will print instructions when called
def instructions():
    print()
    print("Welcome to Rizzos math quiz.")
    print("There are 5 modes you can choose:")
    print()
    print("- Addition, a: 10 points for being correct")
    print("- Subtraction, s: 25 points for being correct")
    print("- Multiplication, m: 50 points for being correct")
    print("- Division, d: 50 points for being correct")
    print("- All, '': 50 points for being correct")
    print()
    print("Try to answer as many questions as possible.")
    print("You can have a timer and see if you can do ")
    print("all the questions in the set time. Every")
    print("incorrect question removes 10 points.")
    return ""


# Main routine
# asks if user has played before
# if no print instructions 
played_before = yes_no("Have you played before? ")
if played_before == "no":
    instructions()
print()
print("Enjoy!")