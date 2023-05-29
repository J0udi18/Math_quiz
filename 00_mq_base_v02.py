# Imports
import random
import time


# Functions go here
# Checks which questions user would like to answer
def string_checker(question, list, error):

        valid = False
        while not valid:
            try:
                # ask user for choice (.lower choice)
                response = input(question).lower()

                # iterates through list and if response is an item
                # in the list (or the first letter of an item), the
                # full item name is returned

                for item in list:
                    if response == item[0] or response == item:
                        return item
                
                # print error if not in list
                print(error)
                print()     

            except IndexError:
                # output error message
                print(error)
                print()


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
            
            # Checks if they inputed correct number
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
def question(symbol, points_val):

    valid = False
    while not valid:

        # Question error if they input unexpected values
        q_error = "Please enter an interger between 0 - 1000 (dont be dumb)"

        # Generate random intergers
        temp_int = random.randint(1, 10)
        int_i = random.randint(1, 10)
        int_ii = temp_int * int_i

        to_ask = "{} {} {} = ".format(int_ii, symbol, int_i)

        # Get answer and there answer to the question
        ans = eval(str(int_ii) + symbol + str(int_i))
        response = num_check(to_ask, q_error, int, "xxx",  -1, 1001)

        # If user quits
        if response == "xxx":
            print("You quit")
            result = "quit"
            return [to_ask, ans, result, response]

        # check if user got answer correct
        if response == ans and time.time() - start < seconds:
            statement_generator("You got it right! +{} points".format(points_val), "*", "~")
            result = "correct"

        elif response != ans and time.time() - start < seconds:
            statement_generator("You got it wrong. -10 points", "|", "-")
            result = "incorrect"

        else:
            statement_generator("Time ran out no points", "|", "-")
            result = "Time out"
            
        print()
        return [to_ask, ans, result, response]


# function will print instructions when called
def instructions():
    statement_generator("Instructions", "|", "-")
    print("There are 5 modes you can choose:")
    print()
    print("- Addition, a: 10 points for being correct")
    print("- Subtraction, s: 25 points for being correct")
    print("- Multiplication, m: 50 points for being correct")
    print("- Division, d: 50 points for being correct")
    print("- All, ' ': 50 points for being correct")
    print()
    print("Try to answer as many questions as possible.")
    print("You can have a timer and see if you can do ")
    print("all the questions in the set time. Every")
    print("incorrect question removes 10 points.")
    print()
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


# main routine
statement_generator("Welcome to Rizzos Math Quiz", "!", "=")

# define the saved points 
save_points = 0

# question type error and yes_no error
ques_type_error = "Error please say either a, s, m, d, or enter for all"
yes_no_error = "<error> Please say yes or no"

# lists
ques_type_list = ["addition", "subtraction", "multiplication", "division", ""]
yes_no_list = ["yes", "no"]
symbol_list = ["+", "-", "*", "/"]

# asks if user has played before
# if no print instructions 
played_before = string_checker("Have you played before? ", yes_no_list, yes_no_error)
if played_before == "no":
    instructions()
print("Enjoy!")

# Main quiz code
play_again = "yes"
while play_again == "yes":

    # reset variables
    questions_answered = 0
    correct_questions = 0
    incorrect_questions = 0
    points = 0
    questions_list = []

    # ask user for which type of questions they would like
    question_type = string_checker('Which type of questions would you like? (a, s, m, d, "") ', ques_type_list, ques_type_error)

    # ask uesr for number of questions
    num_questions_error = "<error> enter an interger"
    num_questions = num_check("How many questions? ", num_questions_error, int, None, 0)
    
    # ask user if they want a timer 
    time_set = string_checker("Would you like a timer? ", yes_no_list, yes_no_error)

    if time_set == "yes":
        # Ask user for the amount of time they get for the questions
        seconds = num_check("how many seconds? ", "enetr an number between 1, 60", int, None, 0, 61)
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
            result = question("*", 50)
            num_points = 50
        elif question_type == "d":
            result = question("/", 50)
            num_points = 50
        else:
            result = question(random.choice(symbol_list), 50)
            num_points = 50
        
        # Add number of questions answered
        questions_answered += 1

        asked = result[0]   # question from list
        user_ans = result[3]    # users answer, from list
        outcome = result[2] # third item of list

        # Add number of correct and incorrect questions
        if outcome == "correct":
            correct_questions += 1
            points += num_points
        elif outcome == "incorrect":
            incorrect_questions += 1
            points -= 10
        elif outcome == "quit":
            questions_list.append("Question #{}: {}{} - {}".format(questions_answered, asked, user_ans, outcome))
            break
        else:
            questions_list.append("Question #{}: {}{} - {}".format(questions_answered, asked, user_ans, outcome))
            break


        # Add question result to a list
        questions_list.append("Question #{}: {}{} - {}".format(questions_answered, asked, user_ans, outcome))
        
        # number of questions left go down
        num_questions -= 1
    
    # **** Calculate Game Stats ****
    percent_correct = correct_questions / questions_answered * 100
    percent_incorrect = incorrect_questions / questions_answered * 100

    # Displays game stats with % values to the nearest whole number
    print()
    statement_generator("Quiz Statistics", "-", "*")
    print("Correct: {}: ({:.0f}%)\nIncorrect: {}: ({:.0f}%)".format(correct_questions, percent_correct, incorrect_questions, percent_incorrect))
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
    show_history = string_checker("Would you like to see game history? ", yes_no_list, yes_no_error)

    # displays history if user says yes
    if show_history == "yes":
        print()
        statement_generator("Quiz History", "-", "*")
        for quiz in questions_list:
            print(quiz)

        print()
        statement_generator("Thanks for playing", "!", "=")

    # Doesnt display history if user says no
    elif show_history == "no":
        print()
        statement_generator("Thanks for playing", "!", "=")
    
    # Ask user if they want to play again
    print()
    play_again = string_checker("Would you like to play again? ", yes_no_list, yes_no_error)
    if play_again == "yes":
        print()
        continue
    else:
        play_again = "no"
# finish