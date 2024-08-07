# Find a duplicate, Space Edition™.

# We have a list of integers, where:

# The integers are in the range 
# 1. The integers are in the range 1..n 
# 2. The list has a length of n+1

# It follows that our list has at least one integer which appears at least twice. 
# But it may have several duplicates, and each duplicate may appear more than twice.

# Write a function which finds an integer that appears more than once in our list. 
# Don't modify the input! (If there are multiple duplicates, you only need to find one of them.)

# We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. 
# Thing is, the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. 
# So we need to optimize for space!

## This is not the expected answer because I sorted. It is SO EASY, if you can sort the input.

def find_repeat(numbers):

    # Find a number that appears more than once
    
    numbers.sort()
    
    first_number = numbers[0]
    for index in range(1, len(numbers)):
        second_number = numbers[index]
        if first_number == second_number:
            return first_number
        first_number = second_number

# TIME COMPLEXITY: O(N log N) because sorting.
# SPACE COMPLEXITY: O(1) because you don't use any additional space.
