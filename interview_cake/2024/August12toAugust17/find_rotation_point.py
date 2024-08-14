# I want to learn some big words so people think I'm smart.

# I opened up a dictionary to a page in the middle and started flipping through, 
# looking for words I didn't know. I put each word I didn't know at increasing 
# indices in a huge list I created in memory. When I reached the end of the dictionary, 
# I started from the beginning and did the same thing until I reached the page I started at.

# Now I have a list of words that are mostly alphabetical, except they start somewhere in 
# the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. 
# In other words, this is an alphabetically ordered list that has been "rotated." For example:

#   words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

# Write a function for finding the index of the "rotation point," which is where I started working 
# from the beginning of the dictionary. This list is huge (there are lots of words I don't know) 
# so we want to be efficient here.
                                                                                                                                                          
def find_rotation_point(words):    
    # General properties of Binary Search:
    # left/low
    # right/high
    # while loop, usually <, sometimes <= with pivots
    # midpoint
    # reset low or high -/+

    first_word = words[0] # ptolemaic
    left = 0
    right = len(words) - 1
    
    # check if it needs to be <= or <
    while left <= right:
        midpoint = (left + right) // 2
        midpoint_word = words[midpoint]
        if midpoint_word < first_word:
            right = midpoint - 1
        # midpoint_word > first_word
        else:
            left = midpoint + 1

        # ITERATION 1
        # 0, 11
        # 0 + 11 = 11 // 2 = 5
        # nums[5] = asymptote
        # asymptote < ptolemaic
        # move right lower
        # right = mid - 1 = 5 - 1 = 4
        # ITERATION 2
        # 0, 4
        # 0 + 4 = 4 // 2 = 2
        # nums[2] = 'supplant'
        # supplant > ptolemaic
        # move left higher
        # left = mid + 1 = 2 + 1
        # ITERATION 3:
        # 3, 4
        # 3 + 4 = 7 // 2 = 3
        # nums[3] = 'udulate'
        # udulate > ptolemaic
        # move left higher 
        # left = 3 + 1 = 4
        # loop ends
        
    return left

# TIME COMPLEXITY: O (LOG N)
# SPACE COMPLECITY: O(1)


# BONUS QUESTION: This function assumes that the list is rotated. If it isn't, what index will it 
# return? How can we fix our function to return 0 for an unrotated list?

# My original answer that passes test cases:
def find_rotation_point(words):

    first_word = words[0]
    left = 0
    right = len(words) - 1
    
    # check if it needs to be <= or <
    while left <= right:
        midpoint = (left + right) // 2
        midpoint_word = words[midpoint]
        if midpoint_word < first_word:
            right = midpoint - 1
        # midpoint_word > first_word
        else:
            left = midpoint + 1
        
    if left == len(words):
        return 0
    return left

# A clearer answer:

def find_rotation_point(words):

    first_word = words[0]
    last_word = words[-1]
    
    if first_word < last_word:
        # not rotated
        return 0
        
    left = 0
    right = len(words) - 1
    
    # check if it needs to be <= or <
    while left <= right:
        midpoint = (left + right) // 2
        midpoint_word = words[midpoint]
        if midpoint_word < first_word:
            right = midpoint - 1
        # midpoint_word > first_word
        else:
            left = midpoint + 1
        
    if left == len(words):
        return 0
    return left

