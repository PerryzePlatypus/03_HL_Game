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

secret = 7

low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []

guess = ""
while guess != secret and guesses_used < guesses_allowed:
# ask the user to guess the number
    guess = int_check("Guess:", low_num, high_num, exit_code= "xxx")
    # check that they don't want quit
    if guess == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break


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

        if guess < secret and guesses_used < guesses_allowed:
            feedback = (f"Too low,please try a lower number."
                        f"You've used {guesses_used} / {guesses_allowed} guesses")
        elif guess > secret and guesses_used < guesses_allowed:
            feedback= (f"Too high, please try a lower number. "
                       f"You've used {guesses_used} / {guesses_allowed} guesses")

        elif guess == secret:

            if guesses_used == 1:
                feedback = " LUCKY YOU! You got in on the first guess"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it in {guesses_used} guesses."
            else:
                feedback = f" Well done! You guessed the secret number in {guesses_used} guesses"

        else:
            feedback = "Sorry - You have no more guesses left. You lose this round!"

        print(feedback)

        if guesses_used == guesses_allowed - 1:
            print("\n CAREFUL! - You have one guess left!")

