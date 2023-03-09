def num_check(question):
    valid = False
    while not valid:

        var_error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response in money:
                return response

            else:
                print(var_error)
                print()

        except ValueError:
            print(var_error)
            print()


played = ""

error = "please enter yes or no as your response"

print("")
print("***Lucky Unicorn***")
print("")
print("")

while played == "":

    yes_response = ["yes", "y"]
    no_response = ["no", "n"]

    played = input("have you played Lucky Unicorn before: ").lower()

    if played in yes_response:

        print()
        conform = input("Do you remember the rules / how to play: ").lower()

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
        conform = input("Press <enter> to start the game.").lower()


    else:
        print("")
        print(error)
        print("")
        played = ("")

conform = ("")

while conform == "":

    if conform in yes_response:

        print("")

    elif conform in no_response:

        print("")
        print("Ok here are the rules / instructions")
        print("first input the amount of money you would like to start")
        print("the game with. then fore every dollar you entered/have you get")
        print("one turn. every turn you a random animal name will show, ")
        print("with unicorn = 5$, zebra and horse = 50c, donkey = 0$.")
        print("")
        print("after reading the instructions pleas enter the amount")
        print("of money you would like to start the game with then ")
        print("Press <enter> to start the game.")

    else:
        print("")
        print(error)
        conform = ""

print("")
money = num_check("enter the amount you would like to start the game with: ")
