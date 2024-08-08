# 211. Add and Search Word - Data structure design
# https://leetcode.com/problems/add-and-search-word-data-structure-design/

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.endSymbol = "*"

    def __add_substring__(self, i, word: str) -> None:
        """
        Adds a word to the trie
        """
        node = self.root
        for j in range(i, len(word)):
            letter = word[j]
            if letter == '.':
                continue
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node.endSymbol = True

    def addWord(self, word: str) -> None:
        """
        Adds a word into the trie
        """
        for i in range(len(word)):
            self.__add_substring__(i, word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        for letter in word:
            if letter == '.':
                letter = node.keys()[0]
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

{'b': {
    'a': {
        'd': {
            '*': True}
        }
    }, 
 'a': {
    'd': {
        '*': True
        }
    }, 
 'd': {
    '*': True, 
    'a': {
        'd': {
            '*': True
            }
        }
    }, 
    'm': {
        'a': {
            'd': {
                '*': True
                }
            }
        }
}

