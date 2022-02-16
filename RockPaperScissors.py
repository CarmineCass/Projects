import random

def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's'and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

def rock_paper_scissors():
    player = input("What is your choice - 'r for rock, 's' for scissors, 'p' for paper: ")
    choices = ['r', 's', 'p']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"It's a tie! Choice is {opponent}")
    if check_win(player, opponent):
        return print(f"Yay! You won! Choice is {opponent}")
    if check_win(player, opponent) != True:
        return print(f"You lost! Choice is {opponent}")


rock_paper_scissors()
