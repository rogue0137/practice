# Write a function for doing an in-place ↴ shuffle of a list.

import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    len_of_the_list = len(the_list)
    if len_of_the_list < 2:
        return the_list
    
    last_index_in_the_list = len_of_the_list - 1
    # forward walkthrough
    for index in range(last_index_in_the_list):
        current_number = the_list[index]
        random_index = get_random(index, len_of_the_list)
        random_number = the_list[random_index]
        
        the_list[index] = random_number
        the_list[random_index] = current_number

# Interview Cake says the above is a famous algo called the
# Fisher-Yates shuffle/ Knuth shuffle.
# In the Interview Cake solution, there is also a check that I've excluded above,
# but am reproducing below. If the number is the same,
# you skip the switch. It's not needed for the test cases,
# but it's probably a good idea
def shuffle(the_list):

    len_of_the_list = len(the_list)
    if len_of_the_list < 2:
        return the_list
    
    last_index_in_the_list = len_of_the_list - 1
    # forward walkthrough
    for index in range(last_index_in_the_list):
        current_number = the_list[index]
        random_index = get_random(index, len_of_the_list)
        random_number = the_list[random_index]
        
        # ADDITIONAL CHECK
        if current_number != random_number:
            the_list[index] = random_number
            the_list[random_index] = current_number
