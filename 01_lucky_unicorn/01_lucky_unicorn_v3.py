import random


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


# Asks the user if they have played before and displays instructions is they haven't
def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        if response == "no" or response == "n":
            return "no"

        # gives an error if player enters an invalid answer
        else:
            print("")
            print(error)
            print("")


# function that displays instructions
def instructions():

    statement_generator("Here are the rules", "-")
    print('''
    
- It costs $1 to play
- If you get a unicorn, you get $5:00 back (ie: win $4:00)
- If you get a zebra or a horse, you get 50c back
- Donkey's unlucky - you don't get anything back

Can you beat the odds?    
    ''')


# applies decoration to statements to make
# it easy to separate sections / see what the user has won
def statement_generator(statement, decoration, lines=None):
    middle = f'{decoration * 5} {statement} {decoration * 5}'
    top_bottom = f'{decoration * len(middle)}'

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# presets variables

error = "please enter yes or no as your response"
money_play = ""
# displays game title
print("")
statement_generator("Lucky Unicorn", "*")
print("")
print("")

# asks player if they have played before
want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print("")
balance = num_check("How much do you want to play with? ")

start_balance = balance

print(f'You have chosen to play with ${balance:.2f}')
print("")

# main routeen goes here

playing = ""

while playing != "n" or playing != "no":
    chosen_num = random.randint(1, 100)

    if playing == "no":
        print("")
        break

    # Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        decoration = "!"
        balance += 4.00
    elif 6 <= chosen_num <= 37:
        chosen = "horse"
        decoration = "H"
        balance -= 0.50
    elif 38 <= chosen_num <= 69:
        chosen = "zebra"
        decoration = "z"
        balance -= 0.50
    else:
        chosen = "donkey"
        decoration = "D"
        balance -= 1.00

    feedback = f"You got a {chosen}, Balance: ${balance:.2f}"

    statement_generator(feedback, decoration, 1)
    print()

    if balance < 1:
        print("")
        break

    playing = yes_no("would you like to try your luck again: ")

print(f'your star balance was ${start_balance:.2f}')
print(f'your final balance is ${balance:.2f}')
