


# This is not the recommended answer, because I didn't use a set:
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    # set_of_chars = set()
    
    char_counter = {}
    
    for char in list(the_string):
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
        
    
    odd_count_chars = 0
    
    for char, count in char_counter.items():
        if count % 2 == 1:
            odd_count_chars += 1
            if odd_count_chars > 1:
                return False

    return True

# This is the recommended answer using a set:

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1

# This is how I would write it to make it a big easier to read (though notably longer)
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # max one character without a pair
    count_of_unpaired_characters = len(unpaired_characters)
    is_palindrome = count_of_unpaired_characters <= 1
    return is_palindrome

