def yes_no(question):
    # Check users response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response = input(question).lower()

        # checks if user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print( "\n\033[95m [!] Please enter Yes/No [!]\033[0m")


# Main routine
print()
print("↑↑↑ Welcome to the Higher Lower Game ↓↓↓")

# Ask users if they want instructions (check if they say yes/no)
want_instructions = yes_no("Do you want to see the instructions? ")


def instructions():
    """Prints instructions"""

    print("""
      *** ↑↑↑ Higher or Lower Game Instructions ↓↓↓ ***

      To begin, you can choose the number of rounds and 
      either customise the game parameters or go with
      the default game ( the secret number will be in-
      between 1 and 100)

      Then choose how many rounds you would like to play 
      or press <enter> for infinite mode.

      You goal is to try and guess the secret number 
      without running out of guesses.

      Good luck and have fun!


# displays the instructions if the user wants
if want_instructions == "yes":
    instructions()

print()
print("Program continues")