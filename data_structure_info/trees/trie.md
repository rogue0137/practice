# Trie

![Justice to what a Trie is](https://en.wikipedia.org/wiki/Trie#/media/File:Trie_example.svg)

Basics
- type of tree!
- replaces a binary search tree or a hashmap (woah)
- usually a type of stored associated array, where the keyes are usually strings (see the pic; explains well)
- all the descendants of a node share a common prefix, eg. descendents with keys "alex" and "alejandra", both share the nodes "a", "al", and "ale"
- GREAT for full text search

Operations:
- find
- insert


https://leetcode.com/problems/implement-trie-prefix-tree/

```python
"""
Another way of implementing `is_word_end` would be to include a special character at the end of the word and then search for that in the search function. 
"""
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word_end = False
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        # When you get to the last node of the word
        # mark that node as the end of the word
        node.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        # check if this is the end of the word
        word_end = node.is_word_end
        return word_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # because you're only searching if it's included, not
        # if its the end, you automatically return True if you 
        # exit the loop
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```