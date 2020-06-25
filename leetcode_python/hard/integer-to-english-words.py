# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/

input: 1234567
bad output: ['Seven', 'Sixty', 'Hundred', 'Five', 'Thousand', 'Four', 'Thirty', 'Hundred', 'Million', 'Two', None]

class Solution:
    def numberToWords(self, num: int) -> str:
        num_as_list = list(str(num))
        rev_list = num_as_list[::-1]
        ones_dict = dict([(1,'One'), (2,'Two'),(3,'Three'),(4,'Four'), (5,'Five'),(6,'Six'), (7,'Seven'), (8,'Eight'), (9,'Nine')])
        one_ten_dict = dict(One='Eleven',Two='Twelve',Three='Thirteen',Four='Fourteen',Five='Fifteen',Six='Sixteen', Seven='Seventeen', Eight='Eighteen',Nine='Nineteen')
        tens_dict = dict([(2,'Twenty'),(3,'Thirty'),(4,'Forty'), (5,'Fifty'),(6,'Sixty'), (7,'Seventy'), (8,'Eighty'), (9,'Ninety')])
        nums_to_words = []
        for index, num in enumerate(rev_list):
            num = int(num)
            # for every 3 indices, add Hundred
            if (index + 1) % 3 == 0:
                nums_to_words.append('Hundred')
            # for every index after 3, add thousand  
            if index % 3 == 0 and index != 0:
                nums_to_words.append('Thousand')
            # for every 6 indices, add million 
            if (index + 1) % 6 == 0:
                nums_to_words.append('Million')
            # for every 9 indices, add billion
            if (index + 1) % 9 == 0:
                nums_to_words.append('Billion')
            if index in [1, 4, 6, 8]:
                if num != 1:
                    nums_to_words.append(tens_dict.get(num))
                else: 
                    original = nums_to_words[-1] 
                    nums_to_words[-1] = one_ten_dict.get(original)
            else:
                nums_to_words.append(ones_dict.get(num))
        print(nums_to_words)
        rev_nums_to_words = nums_to_words[::-1]
        words_as_str = ' '.join(rev_nums_to_words)
        return words_as_str