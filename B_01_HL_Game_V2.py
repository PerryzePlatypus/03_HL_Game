import math
import random




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
    

    """)

def int_check(question, low=None, high=None, exit_code=None):


    if low is None and high is None:
        error = "Please enter an integer more than 0"


    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    else:
        error = (f"Please enter an integer that"
                 f"is between {low} and {high} (inclusive")

    while True:

        response = input(question).lower()

        if response == exit_code:
            return response

        try:

            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)



def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# main routine

# initialise game variable
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()



print("↑↑↑ Higher or Lower Game ↓↓↓")
print()


num_rounds = int_check( "How many rounds? or <enter for infinite>: ", low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# ask the user if they want default parameters ( Secret number between 0 - 10 )
default_params = yes_no("Do you want to use the default game parameters? ( numbers inbetween 0 - 10 )")
if default_params == "yes":
    low_num = 0
    high_num = 10

else:
    #Allows user to choose the high and low number
    low_num = int_check("Low Number?")
    high_num = int_check("High Number?", low=low_num+1)


guesses_allowed = calc_guesses(low_num, high_num)



# game loop starts here
while rounds_played < num_rounds:

    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ ROUND {rounds_played + 1} ( Infinite Mode )♾️♾️♾️"
    else:
        rounds_heading = f"\n🕹️🕹️🕹️ Round {rounds_played + 1} of {num_rounds} 🕹️🕹️🕹️"

    print(rounds_heading)
    print()

    #Round starts here
    # sets guesses to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want quit
        if guess == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        # if already guessed the same number, it notifies the user and doesn't use another gues
        if guess in already_guessed:
            print(f"You've already guessed {guess}. You've *still* used "
              f"{guesses_used} / {guesses_allowed} guesses")
            continue

        else:
            already_guessed.append(guess)


            if guess < secret and guesses_used < guesses_allowed:
                feedback = (f"Too low, please try a high number"
                        f"You've used {guesses_used} / {guesses_allowed} guesses")

            else:
                already_guessed.append(guess)

            guesses_used += 1
            # if the guessed number is below than the secret number, it tells the user to guess a higher number
            if guess < secret and guesses_used < guesses_allowed:
                feedback = (f"Too low,please try a HIGHER number."
                            f"You've used {guesses_used} / {guesses_allowed} guesses")
            # if the guessed number is higher than the secret number, it tells the user to guess a higher number
            elif guess > secret and guesses_used < guesses_allowed:
                feedback= (f"Too high, please try a LOWER number. "
                           f"You've used {guesses_used} / {guesses_allowed} guesses")

            elif guess == secret:
                # if User guesses the number in one round
                if guesses_used == 1:
                    feedback = " LUCKY YOU! You got in on the first guess🍀🌠🍀"
                # if User guesses the number in the last round
                elif guesses_used == guesses_allowed:
                    feedback = f"Phew! You got it in {guesses_used} guesses. 😨🫣😬"
                else:
                    feedback = f" Well done! You guessed the secret number in {guesses_used} guesses. 😁😄😃"

            else:
                feedback = "Sorry - You have no more guesses left. You lose this round! 😢😭😓"
                # tells the user the secret number
                print("The secret number was:", secret)
                print()

            print(feedback)

# warns the user that there are on their last guess
            if guesses_used == guesses_allowed - 1:
                print("\n CAREFUL! - You have one guess left!")



    print()

    if end_game == "yes":
        break

    rounds_played += 1

    all_scores.append(guesses_used)

    # if users are in infinite mode. increase number of rounds
    if mode == "infinite":
        num_rounds += 1

    history_item = f"Round: {rounds_played} - {feedback}"
    game_history.append(history_item)

if rounds_played > 0:

    # game history / statistic
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)


    #output game statistic
    print("📊📊📊 GAME STATISTICS 📊📊📊")
    print(f" Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f}")
    print()

    see_history = yes_no("\nDo you want to see your game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)

    print()
    print("Thanks for playing!!!🦦")

else:
    print()
    print("Chickened out ( You didn't play any rounds! ) 🤣😂🍗🐔")
