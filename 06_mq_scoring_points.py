# Functions
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


# Main routine
quiz_summary = []

questions_answered = 0
questions_incorrect = 0
questions_correct = 0
points = 0
save_points = 0

for item in range(0, 5):
    result = input("choose result: ")

    if result == "i":
        result = "incorrect"
        questions_incorrect += 1
        points -= 10
    elif result == "c":
        result = "correct"
        points += 50
        questions_correct += 1
    
    questions_answered += 1

    # Adds Game result to a list for history
    quiz_summary.append("Question #{}: {} - {} points".format(questions_answered, result, points))

# **** Calculate Game Stats ****
percent_correct = questions_correct / questions_answered * 100
percent_incorrect = questions_incorrect / questions_answered * 100

# Displays game stats with % values to the nearest whole number
print()
print("**** Quiz Statistics ****")
print("Win: {}: ({:.0f}%)\nLoss: {}: ({:.0f}%)".format(questions_correct, percent_correct, questions_incorrect, percent_incorrect))
print()

# Print and figure out new high score 
if points > save_points:
    print("NEW HIGH SCORE")
print("Total points: ", points)
print()

# save score to compare next time
save_points = points
points = 0

# Asks user if they want to see there history
show_history = yes_no("would you like to see game history? ")

# displays history if user says yes
if show_history == "yes":
    print()
    print("**** Quiz History ****")
    for quiz in quiz_summary:
        print(quiz)

    print()
    print("Thanks for playing")

# Doesnt display history if user says no
elif show_history == "no":
    print()
    print("Thanks for Playing")
