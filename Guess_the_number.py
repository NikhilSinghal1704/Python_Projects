import random


def guess(x=1, y=10):
    random_int = random.randint(x, y)
    return random_int


def computer_guess():
    limit = int(input("Enter the limit for the numer range: "))
    Number = guess(1, limit)
    turns = 0
    while True:
        turns += 1
        user_guess = int(input(f"Guess the number [1 - {limit}]: "))
        if user_guess > Number:
            print("Too High")

        elif user_guess < Number:
            print("Too Low")

        else:
            print(
                f"Correct! It took you {turns} turns to guess the correct answer")
            break


def user_guess():
    limit = int(input("Enter the limit for the numer range: "))
    low = 1
    high = limit
    turns = 0
    while True:
        # print(low, high)
        turns += 1
        guess_int = guess(low, high)
        response = input(
            f"Is your number {guess_int} | If yes then enter 'c' | If no then enter 'H' for higher and 'L' for lower than your number: ")
        # print(response != "C" and guess_int <= low or guess_int >= high)
        if response != "C" and (guess_int <= 1 or guess_int >= limit):
            print("Are you messing with me?")
            break
        elif response == "H":
            high = guess_int - 1
        elif response == "L":
            low = guess_int + 1
        else:
            print(f"Yay! I guess your number in {turns} turns")
            break


if __name__ == "__main__":
    while True:
        who = input(
            '''Who will be guessing the number:\n1. If you will guess the secret number\n2. if computer will guess the secret number\n>>>''')
        if who == '1':
            computer_guess()
            break
        elif who == '2':
            user_guess()
            break
        else:
            print("Wrong input try again:")
