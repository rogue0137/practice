# Write a function that takes a list of characters and reverses the letters in place.

# This passes all the tests, but is NOT what interview cake is looking for.
def reverse_using_python_reverse(list_of_chars):

    # Reverse the input list of chars in place
    return list_of_chars.reverse()

# Interview cake was looking for something akin to this:
def reverse(list_of_chars):

    # Reverse the input list of chars in place
    len_of_list_of_chars = len(list_of_chars)
    
    front_index = 0
    back_index = len_of_list_of_chars - 1
    
    while front_index < back_index:
        
        new_front = list_of_chars[back_index]
        new_back = list_of_chars[front_index]
        
        list_of_chars[front_index] = new_front
        list_of_chars[back_index] = new_back
        
        # move front_index once to the right
        front_index += 1
        # move back index once to the left
        back_index -= 1
    
    return list_of_chars

# Time Complexity: O(n)
# - Ok, so we generally only iterate through HALF of the list w/e the size of the list (n) is
# - However, because the amount of times we iterate is directly proportional to the size of the list, we say it's O(n)

# Space Complexity: O(1)
#  - Since we're doing it in place, we don't use any additional space
