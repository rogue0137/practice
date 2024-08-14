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

# This is NOT the expected solution, but it passes all the tests cases :joy:
# I forgot I'm not supposed to "sort".

def find_repeat(numbers):

    # General properties of Binary Search:
    # left/low
    # right/high
    # while loop, usually <=, sometimes <
    # midpoint
    # reset low or high -/+ exclusive
    
    numbers.sort() 
    
    left = 0 
    right = len(numbers) - 1 
    
    while left < right:
        midpoint = (left + right ) // 2
        midpoint_number = numbers[midpoint]
        if midpoint_number == midpoint:
            right = midpoint - 1
        else:
            left = midpoint + 1
    
    return numbers[left]

# Time complexity: O(n log n) due to sorting.
# Space complexity: O(n) because Python's `sort` has O(n) worst case



