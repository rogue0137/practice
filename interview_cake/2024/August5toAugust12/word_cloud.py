# QUESTION 1: We haven't explicitly talked about how to handle more complicated character sets. 
# How would you make your solution work with more unicode characters? What changes 
# need to be made to handle silly sentences like these:

# I'm singing ♬ on a ☔ day.

# ☹ + ☕ = ☺.

# ANSWER: I would have to change it to use .isalpha(). Right now I am checking specific punctuation marks.
#   I would need to ignore unicode characters now to get the words. I am also just adding to a string
#   below instead of my original adding letters to a list and then joining that list to form a word.

class WordCloudData(object):

    def __init__(self, input_string):
        self.input_string = input_string
        self.words_to_counts = {}
        
        self.count_words()

    def deal_with_punctuation(self, word):
        # Normalize case
        word_lowercased = word.lower()
        
        # Check if the word exists in the dictionary
        if self.words_to_counts.get(word_lowercased) is not None:
            self.words_to_counts[word_lowercased] += 1
        else:
            self.words_to_counts[word_lowercased] = 1

    def count_words(self):
        current_word = ''
        for char in self.input_string:
            # CHECKING HERE for letters. If we're including numbers, use .isalnum() instead
            if char.isalpha():
                current_word += char
            else:
                # If not part of a word, process the accumulated word
                if current_word:
                    self.deal_with_punctuation(current_word)
                    current_word = ''  # Reset for the next word
        
        # Process the last word if the string doesn't end with punctuation
        if current_word:
            self.deal_with_punctuation(current_word)
            
        return self.words_to_counts


# QUESTION 2: We limited our input to letters, hyphenated words and punctuation. 
# How would you expand your functionality to include numbers, email addresses, twitter handles, etc.?
# ANSWER: 
# - Numbers: Use .alnum() above
# - Email addresses: Update `char.isalpha()` to `char.isalpha() or char == '@'`; however, this would not
#   handle dots inside email addresses.
# - Twitter handles: Same as above. We could also expand the `char == '@'` to `char in symbols` where weird_symbols == '@_'
#   if we had underscores and other things.

# QUESTION 3: How would you add functionality to identify phrases or words that belong together but aren't hyphenated? 
# ("Fire truck" or "Interview Cake")

# ANSWER: Oof, NLP anyone?
# Ok, here's the approach:
# 1) Tokenize a la breaking the text up into individual words -- Already done using `count_words()`
# 2) Frequncy analysis -- Already done using `deal_with_punctuation()`
# 3) Co-occurrence Analysis and Phrase Identification -- New stuff. See below.
class WordCloudData(object):

    def __init__(self, input_string):
        self.input_string = input_string
        self.words_to_counts = {}
        self.word_pairs = {}  # To store word pairs and their counts
        self.count_words_and_pairs()  # Call the enhanced method to count words and identify pairs

    def deal_with_punctuation(self, word):
        # Normalize case
        word_lowercased = word.lower()
        
        # Check if the word exists in the dictionary
        if self.words_to_counts.get(word_lowercased) is not None:
            self.words_to_counts[word_lowercased] += 1
        else:
            self.words_to_counts[word_lowercased] = 1

    def count_words_and_pairs(self):
        current_word = ''
        prev_word = None

        for char in self.input_string:
            if char.isalnum():
                current_word += char
            else:
                if current_word:  # current_word is not empty
                    self.deal_with_punctuation(current_word)
                    # Update word pairs count
                    if prev_word is not None:
                        pair = (prev_word.lower(), current_word.lower())
                        if pair in self.word_pairs:
                            self.word_pairs[pair] += 1
                        else:
                            self.word_pairs[pair] = 1
                    prev_word = current_word  # Update prev_word for the next iteration
                    current_word = ''  # Reset for the next word

        # Process the last word if the string doesn't end with punctuation
        if current_word:
            self.deal_with_punctuation(current_word)
            if prev_word is not None:
                pair = (prev_word.lower(), current_word.lower())
                if pair in self.word_pairs:
                    self.word_pairs[pair] += 1
                else:
                    self.word_pairs[pair] = 1

        self.identify_phrases()

        return self.words_to_counts

    def identify_phrases(self):
        # Simple heuristic: pairs occurring more than twice as phrases
        # You could literally pick any number. You plus your interviewer are deciding the heuristic
        phrases = { pair: count for pair, count in self.word_pairs.items() if count > 2}
        return phrases



# QUESTION 4: How could you improve your capitalization algorithm?
# ANSWER: I'm not sure how it could be improved. I am testing for upper case, lower case, and title case,
#   which seem to be all the possibilities of cases so far. If other cases were included, I 
#   could use the python methods related to those.

# QUESTION 5: How would you avoid having duplicate words that are just plural or singular possessives?
