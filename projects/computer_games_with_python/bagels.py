# TODO: Add validations


import random

intro = """
Welcome to Bagels! I am thinking of a 3-digit number. Try to guess what it is. Here are some clues:

When I say:    That means:
    Fermi        Right number, right position.
    Pico         Right number, but wrong position.
    Bagels       Not the right number.

I have thought up a number. You have 10 guesses to get it.
"""

possible_outcomes = {
    'bagels': 'Bagels',
    'fermi': 'Fermi',
    'pico': 'Pico',
    'win': 'Win'
}

def validate_guess(guess):
    validated = True
    if len(guess) != 3:
        print('Please enter three digits only')
        validated = False
    
    try:
        int(guess)
    except: 
        print('Please enter a valid string')
        validated = False

    return validated
    


def process_guess(guess, split_number):
    split_guess = list(map(int, guess))

    outcome = []

    # first check if any digits are correct
    for x in split_guess:
        print(f'x in split guess : {x}')
        if x in split_number:
            outcome.append(possible_outcomes['pico'])
        else: 
            outcome.append(possible_outcomes['bagels'])
    
    same_as_secret_number_counter = 0
    # check if any digits are the in right position
    if possible_outcomes['pico'] in outcome:
        if split_guess[0] == split_number[0]:
            same_as_secret_number_counter += 1
            outcome[0] = possible_outcomes['fermi']
        if split_guess[1] == split_number[1]:
            same_as_secret_number_counter += 1
            outcome[1] = possible_outcomes['fermi']
        if split_guess[2] == split_number[2]:
            same_as_secret_number_counter += 1
            outcome[2] = possible_outcomes['fermi']
    
    if same_as_secret_number_counter == 3:
        outcome.append(possible_outcomes['win'])

    return outcome

    
def playAgain():
    answer = input('Do you want to play again?')
    lowercased_answer = answer.lower()
    if lowercased_answer.startswith('y'):
        playBagels()

def playBagels():
    #SET UP GAME
    SECRET_NUMBER = random.randint(100, 999)
    split_number = list(int(x) for x in str(SECRET_NUMBER))
    WIN = False
    GUESSES = 0

    print(intro)
    while GUESSES < 10 and not WIN:
        GUESSES += 1
        guess = input(f'Guess #{GUESSES}: ')
        validated_guess = validate_guess(guess)
        if validated_guess:
            outcome = process_guess(guess, split_number)
            # this should be includes ['win']
            if possible_outcomes['win'] in outcome:
                print('You got it!')
                WIN = True
                playAgain()
            else:
                print(outcome)
    
    if not WIN:
        print('You\'re out of turns.')
        print(f' The secret number is {SECRET_NUMBER}.')
        playAgain()
            






playBagels()
