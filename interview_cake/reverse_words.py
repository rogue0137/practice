# Your team is scrambling to decipher a recent message, worried it's a plot to break
# into a major European National Cake Vault. The message has been mostly deciphered,
# but all the words are backward! Your colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a message as a list of characters and
# reverses the order of the words in place. 


# Actual function
def reverse_words(message):

    space = ' '
    if (space not in message):
        return message
    
    # reverse all characters
    len_of_message = len(message)
    front_index = 0
    back_index = len_of_message - 1
    reverse_characters(message, front_index, back_index)
    
    # reverse characters within words
    current_word_starting_index = 0
    
    for index in range(len(message) + 1):
        if (index == len(message)) or (message[index] == space):
            reverse_characters(
                message, 
               current_word_starting_index, 
                index - 1
                )
            current_word_starting_index = index + 1
    
    return message

# Helper Function
def reverse_characters(
    message_or_word, front_index, back_index):
    
    # reverse characters
    while front_index < back_index:
        new_front = message_or_word[back_index]
        new_back = message_or_word[front_index]
        
        message_or_word[front_index] = new_front
        message_or_word[back_index] = new_back
        
        front_index += 1
        back_index -= 1

# Time Complexity:
# - Each character is processed twice; first when the characters are reversed
#   and, second, when the characters in each word are reversed
# - This is technically O(2n), but since we don't care about the 2, it becomes O(n)
# - Why don't we care about the 2? Big O doesn't care about the total operations,
#   but rather the rate of growth of the algorithm
# Space Complexity: O(1)
# - we're using the same list so we're not using any additional space







