# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/


# HASHING APPROACH: Review again
class Solution:
    def all_valid_prefixes(self, word):
        valid_prefixes = []
        for i in range(len(word)):
            word_beg_at_i = word[i:]
            reversed_word = word_beg_at_i[::-1]
            if word_beg_at_i == reversed_word:
                word_up_to_i = word[:i]
                valid_prefixes.append(word_up_to_i)
        return valid_prefixes

    def all_valid_suffixes(self, word):
        valid_suffixes = []
        for i in range(len(word)):
            word_up_to_i_plus_one = word[:i+1]
            reversed_word = word_up_to_i_plus_one[::-1]
            if word_up_to_i_plus_one == reversed_word:
                word_ending_at_i_plus_one = word[i + 1:]
                valid_suffixes.append(word_ending_at_i_plus_one)
        return valid_suffixes

    def palindromePairs(self, words):
        word_lookup = dict()

        # iterate through words adding them to lookup dict
        # key: word, value: index
        # 1N
        for i, word in enumerate(words):
            word_lookup[word] = i
        solutions = []

        palindrome_indices = []

        # 2N, no longer N^2
        for word_index, word in enumerate(words):
            reversed_word = word[::-1]

            # CASE 1:
            # Word 1 is reverse of Word 2
            # Word 2 is reverse of Word 1
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                palindrome_indices.append([word_index, word_lookup[reversed_word]])

            # CASE 2:
            # Word 1 is shorter
            # Word 2 must include the reverse of Word 1 and a palindrome
            for suffix in self.all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    palindrome_indices.append([word_lookup[reversed_suffix], word_index])

            # CASE 3:
            # Word 2 is shorter
            # Word 1 must include the reverse of Word 1 and palindrome
            for prefix in self.all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    palindrome_indices.append([word_index, word_lookup[reversed_prefix]])

        return palindrome_indices
# Runtime: 716 ms, faster than 52.74% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 15.1 MB, less than 38.96% of Python3 online submissions for Palindrome Pairs.




# BRUTE FORCE APPROACH: Does not pass time limit 
from collections import deque

class Solution:
    def is_palindrome(self, new_word):
        queue = deque(new_word)

        while len(queue) > 1:
            pop_left = queue.popleft()
            pop_right = queue.pop()
            if pop_left != pop_right:
                return False
        
        return True

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_len = len(words)
        palindrome_indices = []
        for i in range(words_len):
            first_word = words[i]
            for j in range(words_len):
                if i == j:
                    continue
                second_word = words[j]
                new_word = first_word + second_word
                if self.is_palindrome(new_word):
                    palindrome_indices.append([i, j])

        return palindrome_indices


# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#         # do trie answer for practice!