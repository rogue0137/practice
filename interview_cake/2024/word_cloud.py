# QUESTION:

# You want to build a word cloud, an infographic where the size of a word corresponds to how 
# often it appears in the body of text.

# To do this, you'll need data. Write code that takes a long string and builds its word cloud 
# data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.

# Think about capitalized words. For example, look at these sentences:

# 'After beating the eggs, Dana read the next step:'
# 'Add milk and eggs, then add flour and sugar.'

# What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should 
# include one "Add" or "add" with a value of 2. Make reasonable (not necessarily perfect) decisions about 
# cases like "After" and "Dana".

# Assume the input will only contain words and standard punctuation.

 
# The below solution passes test cases, but is not the recommended solution
# Additionally, this is a test case:
def test_ellipses_between_words(self):
    input = 'Mmm...mmm...decisions...decisions'

    word_cloud = WordCloudData(input)
    actual = word_cloud.words_to_counts

    expected = {'Mmm': 2, 'decisions': 2}
    self.assertEqual(actual, expected)

# I changed it to the following because based on the example in the question, we could use "Add" or "add"
# I chose to keep all keys as whatever they were the first time we encountered them
def test_ellipses_between_words(self):
    input = 'Mmm...mmm...decisions...decisions'

    word_cloud = WordCloudData(input)
    actual = word_cloud.words_to_counts

    # I changed this to Mmm, it was mmm
    expected = {'Mmm': 2, 'decisions': 2}
    self.assertEqual(actual, expected)

#  NOT RECOMMENDED SOLUTION:
class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word
        self.input_string = input_string
        self.words_to_counts = {}
        
        self.count_words()

    def deal_with_punctuation(self, prev_word):
        #  Dashes: We do not include dashes in count_words() punctuation
        #    because we could have hyphenated words. However, if we run into
        #    any solo dashes, we know that they are punctuation not used to 
        #    hyphenate a word.
        dash = '-'
        
        if prev_word != dash: 
        
            # It is possible to have words Lower Cased, Upper Cased and Title Cased
            prev_word_lowercased = prev_word.lower()
            prev_word_uppercased = prev_word.upper()
            prev_word_titlecased = prev_word.title()
            
            isWordAsLowercaseInDict = self.words_to_counts.get(prev_word_lowercased) is not None
            isWordAsUppercaseInDict = self.words_to_counts.get(prev_word_uppercased) is not None
            isWordAsTitleInDict = self.words_to_counts.get(prev_word_titlecased) is not None
            
            if isWordAsLowercaseInDict:
                self.words_to_counts[prev_word_lowercased] += self.words_to_counts[prev_word_lowercased]
            elif isWordAsUppercaseInDict:
                self.words_to_counts[prev_word_uppercased] += self.words_to_counts[prev_word_uppercased]
            elif isWordAsTitleInDict:
                self.words_to_counts[prev_word_titlecased] += self.words_to_counts[prev_word_titlecased]
            else:
                self.words_to_counts[prev_word] = 1

    def count_words(self):
 
        prev_word = []
        # This type of punctuation will tell us that we have potentially finished a word
        punctuation = [' ', '.', ',', ':', '?', '!']
        
        for char in self.input_string:
            if char in punctuation and len(prev_word) > 0:
                prev_word_str = ''.join(prev_word)
                self.deal_with_punctuation(prev_word_str)
                prev_word = []
            elif char in punctuation:
                # Don't do anything if it's punctuation
                continue
            else:
                # print('appending char: ', char)
                prev_word.append(char)

        if len(prev_word) > 0:
            prev_word_str = ''.join(prev_word)
            self.deal_with_punctuation(prev_word_str)
            
        return self.words_to_counts
    
# TIME COMPLEXITY: O(N) because it's dependent on the size of the input in the for loop
# SPACE COMPLEXITY: O(N) because words_to_counts will at most have N number of items if none are duplicates.
