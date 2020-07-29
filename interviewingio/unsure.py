"""
Your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['c', 'c', 'c', 'a', 'r', 's'],
    ['c', 'c', 'i', 't', 'n', 'b'],
    ['a', 'c', 'n', 'n', 't', 'i'],
    ['t', 'c', 'i', 'i', 'p', 't']
]

word1_1 = "catnip"
find_word_location(grid1, word1_1)-> [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]

word1_2 = "cccc"
find_word_location(grid1, word1_1)-> [(0, 1), (1, 1), (2, 1), (3, 1)]
OR [(0, 0), (1, 0), (1, 1), (2, 1)]
OR [(0, 0), (0, 1), (1, 1), (2, 1)]
OR [(1, 0), (1, 1), (2, 1), (3, 1)]


grid2 = [
    ['c', 'p', 'a', 'n', 't', 's'],
    ['a', 'b', 'i', 't', 'a', 'b'],
    ['t', 'f', 'n', 'n', 'c', 'i'],
    ['x', 's', 'c', 'a', 't', 'n'],
    ['x', 's', 'd', 'd', 'e', 'a'],
    ['s', 'q', 'w', 'x', 's', 'p']
]


word2 = "catnap"
find_word_location(grid2, word2)-> [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]

grid3 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'i'],
    ['t', 'f', 'n', 'n', 'x', 'p'],
    ['x', 's', 'i', 'x', 'p', 't']]
    
    c : [0,0 0,2]
    a: [0,3]
    t: [1,3]
word3 = "catnip"
find_word_location(grid3, word3)-> [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]

"""

def find_word_location(grid, word): 
    location_array = []
    word_array = list(word)
    # ["c", "a", "t", "n", "i", "p"]
    # 0, 1, 2, 3... n

    height = len(grid)
    width = len(grid[0])
    
    L = 0
    char = word_array[0]
    
    for i in range(width):
        for j in range(height):
            comp_char = grid[i][j]
            print(comp_char)
            # if comp_char == char:
                # add (i,j) tuple to location_array
                # if last one; break
                # else: increment char one to the right

    
    
    return location_array




grid1 = [
    ['c', 'c', 'c', 'a', 'r', 's'],
    ['c', 'c', 'i', 't', 'n', 'b'],
    ['a', 'c', 'n', 'n', 't', 'i'],
    ['t', 'c', 'i', 'i', 'p', 't']
]
word1_1 = "catnip"
word1_2 = "cccc"

find_word_location(grid1, word1_1)

grid2 = [
    ['c', 'p', 'a', 'n', 't', 's'],
    ['a', 'b', 'i', 't', 'a', 'b'],
    ['t', 'f', 'n', 'n', 'c', 'i'],
    ['x', 's', 'c', 'a', 't', 'n'],
    ['x', 's', 'd', 'd', 'e', 'a'],
    ['s', 'q', 'w', 'x', 's', 'p']
]
word2 = "catnap"

grid3 = [
    ["c","r","c","a","r","s"],
    ["a","b","i","t","n","i"],
    ["t","f","n","n","x","p"],
    ["x","s","i","x","p","t"]
]
word3 = "catnip"


from collections import Counter


def find_embedded_word(words, string):
    # n : len(words), s : len(string), m : maximum word length 
    # TIME: S + (N * M) 
    # SPACE: N
    string_counter = Counter(string) 
    # print(f'counter: {string_counter}')
    
    for word in words: # 
        len_word = len(word) # 1
        word_counter = Counter(word) # 1
        counter_len = len(word_counter) # 1 
        matching_chars = []
        # print(f'word counter: {word_counter}')
        for char in word_counter: # 
            word_val = word_counter[char]
            #print(f'word_val: {word_val}')
            str_val = string_counter.get(char, 0)
            #print(f'str_val: {str_val}')
            if str_val < word_val:
                break
            else: 
                counter_len -= 1
                if counter_len == 0:
                    return word
            # checked last character, we're good
            # return word
    
    return None

# words = ["cat", "dog", "bird", "car", "ax", "baby"]
# string1 = "tcabnihjs"
# string2 = "tbcanihjs"
# string3 = "baykkjl"
# string4 = "bbabylkkj"

# assert find_embedded_word(words, string1) == 'cat'
# assert find_embedded_word(words, string2) == 'cat'
# assert find_embedded_word(words, string3) == None
# assert find_embedded_word(words, string4) == 'baby'



