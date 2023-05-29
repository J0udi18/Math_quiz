# functions go here

def get_question():
    ask = input("Colour? ")
    colour_list.append(ask)


# main routine goes here

thing = input("Timed??")

colour_list = []

if thing == "yes":
    for item in range(0, 3):
        get_question()

else:
    for item in range(0, 1):
        get_question()

print(colour_list)