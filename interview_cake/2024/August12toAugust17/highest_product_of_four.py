# What if we wanted the highest product of 4 items?

from functools import reduce
from operator import mul

def highest_product_of_four(list_of_ints):
    # If the list was not a sorted list, I'd add the below:
    # list_of_ints.sort()

    if len(list_of_ints) < 4:
        raise ValueError('The input needs to be at least four integers')

    if len(list_of_ints) == 4:
        return reduce(mul, list_of_ints)
    
    # There are two possible ways to get highest product of four
    # 1) Four positive numbers
    # 2) Two positive numbers and two negative numbers
    # 3) Four negative numbers

    highest_number = list_of_ints[-1]
    second_highest_number = list_of_ints[-2]
    third_highest_number = list_of_ints[-3]
    fourth_highest_number = list_of_ints[-4]

    lowest_number = list_of_ints[0]
    second_lowest_number = list_of_ints[1]
    third_lowest_number = list_of_ints[2]
    fourth_lowest_number = list_of_ints[3]

    highest_product_from_positive_numbers = (highest_number * second_highest_number * 
                                             third_highest_number * fourth_highest_number)    
    highest_product_from_positive_and_negative_numbers = ( highest_number * second_highest_number *
                                                         lowest_number * second_lowest_number)
    highest_product_from_negative_numbers = (lowest_number * second_lowest_number *
                                             third_lowest_number * fourth_lowest_number)
    
    max_product_of_four = max(highest_product_from_positive_numbers,
                              highest_product_from_positive_and_negative_numbers,
                              highest_product_from_negative_numbers)

    return max_product_of_four
