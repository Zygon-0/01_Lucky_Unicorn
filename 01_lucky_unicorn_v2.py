# checks if numbers are valid
def num_check(question):
    valid = False
    while not valid:

        var_error = "Please enter a number that is less then ten but more than zero"

        try:

            response = float(input(question))

            if 1 <= response <= 10:
                return response

            else:
                print(var_error)
                print()

        except ValueError:
            print(var_error)
            print()

# presets variables


played = ""
money = ""
error = "please enter yes or no as your response"

# displays game title

print("")
print("***Lucky Unicorn***")
print("")
print("")

# asks player if they have played before

while played == "":

    yes_response = ["yes", "y"]
    no_response = ["no", "n"]

    played = input("have you played Lucky Unicorn before: ").lower()

    if played in yes_response:

        print()

    elif played in no_response:

        print("")
        print("Ok here are the rules / instructions")
        print("first input the amount of money you would like to start")
        print("the game with. then fore every dollar you entered/have you get")
        print("one turn. every turn you a random animal name will show, ")
        print("with unicorn = 5$, zebra and horse = 50c, donkey = 0$.")
        print("")
        print("after reading the instructions pleas enter the amount")
        print("of money you would like to start the game with then ")
        money = num_check("Press <enter> to start the game: ")
        print("")

# gives an error if player enters an invalid answer

    else:
        print("")
        print(error)
        print("")
        played = ""

# asks player for the amount ow money they would like to start with if necessary

while money == "":

    money = num_check("enter the amount you would like to start the game with: ")
