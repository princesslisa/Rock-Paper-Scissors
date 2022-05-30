import random

name = input("Welcome to Rock-Paper-Scissors.\n\nPlease enter your name: ")

game = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

opt = list(game)

# Input loop
while True:
    user = input('\nPick "R" for rock, "P" for paper, "S" for scissors: ')
    CPU = random.choice(opt)

    if user not in opt:
        print("You didn't choose a valid option. Please try again\n")
    elif user == CPU:
        print("It's a tie. Please play again.\n")
    else:
        print('\n{} ({}) : CPU ({})'.format(name, game[user], game[CPU]))
        win = user + CPU

        if win in ['RS', 'PR', 'SP']:
            print('{} beats {} \n\nWINNER: {}'.format(game[user], game[CPU], name))
        elif win in ['SR', 'RP', 'PS']:
            print('{} beats {} \n\nWINNER: CPU'.format(game[CPU], game[user]))

        break




