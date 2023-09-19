import random

def check_win(user, computer):
    if user == "r" and computer == "s":
        return True
    elif user == "p" and computer == "r":
        return True
    elif user == "s" and computer == "p":
        return True
    return False

def play(x):
    user_score = 0
    computer_score = 0
    i = x
    moves = ["r", "p", "s"]
    while i:
        computer = random.choice(moves)
        
        while True:
            user = input("Enter r: rock, p: paper, s: scissor: ")
            if user in moves:
                break
            else:
                print("Wrong input try again")
                
        if user == computer:
            print("Tie!")
            i += 1
        elif check_win(user, computer):
            print("You Win!")
            user_score += 1
        else:
            print("You Loose!")
            computer_score += 1
        i -= 1
    return computer_score, user_score

if __name__ == "__main__":
    n = int(input("Best of: "))
    computer, user = play(n)
    if user == computer:
        print(f"You and the computer scored same {user}")
    elif user > computer:
        print(f"You win with score of {user}")
    else:
        print(f"You lost, computer's score: {computer}, Your score: {user}")