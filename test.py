from random import shuffle

myList = [' ','O',' ']

def shuffle_list(alist):
    shuffle(alist)
    return alist


def player_guess():
    guessed_index = ''
    while guessed_index not in ['0','1','2']:
        guessed_index = input('Please enter 0, 1, or 2: ')
        return int(guessed_index)

def check_game(alist, index):
    if alist[index] == 'O' :
        print('You won')
    else:
        print('You lost')

    print(alist)

check_game(shuffle_list(myList),player_guess())
