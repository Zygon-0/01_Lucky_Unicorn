# checks users enter an integer between 1 and 10 inclusive
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


# function that asks the user weather they have played before and displays instructions is they haven't
def yes_no():

    response = ""
    while response == "":

        yes_response = ["yes", "y"]
        no_response = ["no", "n"]

        response = input("have you played Lucky Unicorn before: ").lower()

        if response in yes_response:

            print()

        elif response in no_response:

            print("")
            print("Ok here are the rules / instructions")
            print("first input the amount of money you would like to start")
            print("the game with. then fore every dollar you entered/have you get")
            print("one turn. every turn you a random animal name will show, ")
            print("with unicorn = 5$, zebra and horse = 50c, donkey = 0$.")
            print("")
            print("after reading the instructions please enter the amount")
            print("of money you would like to start the game with then ")
            num_check("Press <enter> to start the game: ")
            print("")
            return response

        # gives an error if player enters an invalid answer

        else:
            print("")
            print(error)
            print("")
            response = ""


# presets variables
money = ""
error = "please enter yes or no as your response"

# displays game title
print("")
print("***Lucky Unicorn***")
print("")
print("")

# asks player if they have played before
yes_no()

# asks player for the amount ow money they would like to start with if necessary
while money == "":
    money = num_check("enter the amount you would like to start the game with: ")
