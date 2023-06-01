import random
import time


# Functions go here

# Checks which questions user would like to answer
def question_checker(question):
    valid = False
    while not valid:

        response = input(question).lower()
        # set list  of the type of questions
        ques_type_list = ["a", "s", "m", "d", ""]

        # Checks how long word is
        if response not in ques_type_list:
            print("<error> please first letter of math question eg: a for addition\n"
                  "OR press <enter> for all types of questions")
            print()
            continue
        else:
            return response


# Number checker to make sure user inputs correctly
def num_check(question, error, num_type, exit_code=None, low=None, high=None):
    valid = False
    while not valid:
        try:
            # Checks if user inputs exit code
            response = input(question)
            if response == exit_code:
                return response
            else:
                response = num_type(response)

            # Checks if they inputted correct number
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


# Checks for yes or no responses
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


# Definition that generates questions randomly and will call this function
def question(symbol, points_val):
    valid = False
    while not valid:

        # Question error if they input unexpected values
        q_error = "Please enter an integer between 0 - 1000 (dont be dumb)"

        # Generate random integer
        temp_int = random.randint(1, 10)
        int_i = random.randint(1, 10)
        int_ii = temp_int * int_i

        # Get answer and there answer to the question
        ans = eval(str(int_ii) + symbol + str(int_i))
        response = num_check("{} {} {} = ".format(int_ii, symbol, int_i), q_error, int, "xxx", -1, 1001)

        # If user quits
        if response == "xxx":
            print("You quit")
            result = "quit"
            return result

        # check if user got answer correct
        if response == ans and time.time() - start < seconds:
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            result = "correct"
            print()
            return result
        elif response != ans:
            statement_generator("You got it wrong. -10 points", "|", "-")
            result = "incorrect"
            print()
            return result
        else:
            statement_generator("Time ran out no points", "|", "-")
            result = "quit"
            print()
            return result


# Function will print instructions when called
def instructions():
    statement_generator("Instructions", "|", "-")
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


# Gives statements decoration on sides and top
def statement_generator(statement, side_decoration, top_bottom_decoration):
    sides = side_decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = top_bottom_decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Timer function stalls program and counts down
def timer(t):
    print("00 : {}".format(t))

    while t != 0:
        t -= 1
        time.sleep(1)
        print("00 : {}".format(t))


# Reset variables
questions_answered = 0
correct_questions = 0
incorrect_questions = 0
points = 0
questions_list = []

# Main routine
statement_generator("Welcome to Joudi's Math Quiz", "!", "=")

print("\033[1;32;40m welcome \n")

# define the saved points 
save_points = 0

# Asks if user has played before
# If no print instructions
played_before = yes_no("Have you played before? ")
if played_before == "no":
    instructions()
print()
print("Enjoy!")

# Main quiz code
play_again = "yes"
while play_again == "yes":

    # Reset variables
    questions_answered = 0
    correct_questions = 0
    incorrect_questions = 0
    points = 0
    questions_list = []

    # Symbol list
    symbol_list = ["+", "-", "*", "/"]

    # Ask user for which type of questions they would like
    question_type = question_checker("Which type of questions would you like? (a, s, m, d, '') ")

    # Ask user for number of questions
    num_questions_error = "<error> enter an integer"
    num_questions = num_check("How many questions? ", num_questions_error, int, None, 0)

    # Ask user if they want a timer
    time_set = yes_no("Would you like a timer? ")

    if time_set == "yes":
        # Ask user for the amount of time they get for the questions
        seconds = num_check("how many seconds? ", "enter an number between 1, 59", int, None, 0, 60)
        print("Timer set! ")
        # Set start
        start = time.time()

    # No timer
    else:
        start = time.time() * 10000
        seconds = 1

    # Generate questions
    while time.time() - start < seconds and num_questions > 0:

        # generates questions depending on what type you choose
        if question_type == "a":
            result = question("+", 10)
            num_points = 10
        elif question_type == "s":
            result = question("-", 25)
            num_points = 25
        elif question_type == "m":
            result = question("x", 50)
            num_points = 50
        elif question_type == "d":
            result = question("/", 50)
            num_points = 50
        else:
            result = question(random.choice(symbol_list), 50)
            num_points = 50

        # Add number of correct and incorrect questions
        if result == "correct":
            correct_questions += 1
            points += num_points
        elif result == "incorrect":
            incorrect_questions += 1
            points -= 10
        else:
            questions_answered -= 1
            break

        # Add number of questions answered
        questions_answered += 1

        # Add question result to a list
        questions_list.append("Question #{}: {}".format(questions_answered, result))

        # number of questions left go down
        num_questions -= 1

    print(questions_answered)
    print(correct_questions)
    print(incorrect_questions)

    # **** Calculate Game Stats ****
    percent_correct = correct_questions / questions_answered * 100
    percent_incorrect = incorrect_questions / questions_answered * 100

    # Displays game stats with % values to the nearest whole number
    print()
    statement_generator("Quiz Statistics", "-", "*")
    print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(correct_questions, percent_correct,
                                                                    incorrect_questions, percent_incorrect))
    print()

    # Print and figure out new high score 
    if points > save_points:
        print("NEW HIGH SCORE")
        save_points = points
    else:
        print("Nice Job!")
    print("Total points: ", points)
    print()

    # Asks user if they want to see there history
    show_history = yes_no("would you like to see game history? ")

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Quiz History", "-", "*")
        for quiz in questions_list:
            print(quiz)

        print()
        statement_generator("Thanks for playing", "!", "=")

    # Doesn't display history if user says no
    elif show_history == "no":
        print()
        statement_generator("Thanks for playing", "!", "=")

    # Ask user if they want to play again
    print()
    play_again = yes_no("Would you like to play again? ")
    if play_again == "yes":
        print()
        continue
    else:
        play_again = "no"

    print("\033[2;32;40m thx for doing the quiz  \n")
