# 1165. Single-Row Keyboard
# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        spaces_to_word = 0
        
        keyboard_as_list = list(keyboard)
        word_as_list = list(word)
        keyboard_dict = dict()
        
        for index, key in enumerate(keyboard_as_list):
            keyboard_dict[key] = index
        
        starting_space = 0
        for char in word:
            char_in_keyboard = keyboard_dict[char]
            if char_in_keyboard > starting_space:
                space_to_add = char_in_keyboard - starting_space
                spaces_to_word += space_to_add
            if char_in_keyboard < starting_space:
                space_to_add = starting_space - char_in_keyboard
                spaces_to_word += space_to_add
            starting_space = char_in_keyboard
        return spaces_to_word


# # using enumerate
# Runtime: 48 ms, faster than 70.68% of Python3 online submissions for Single-Row Keyboard.
# Memory Usage: 13.9 MB, less than 34.04% of Python3 online submissions for Single-Row Keyboard.

# # using range
# Runtime: 44 ms, faster than 84.17% of Python3 online submissions for Single-Row Keyboard.
# Memory Usage: 13.9 MB, less than 44.77% of Python3 online submissions for Single-Row Keyboard.
