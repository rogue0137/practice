# 273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/


class Solution:
    def numberToWords(self, num: int) -> str:
        less_than_twenty = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen' }

        less_than_ten = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety' }
        
        one_digit = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine' }

        def two_digits(num):
            if not num:
                return ''
            elif num < 10:
                return one_digit[num]
            elif num < 20:
                return less_than_twenty[num]
            else:
                tens = num // 10
                remainder = num % 10
                if remainder:
                    return less_than_ten[tens] + ' ' + one_digit[remainder]
                else:
                    return less_than_ten[tens]
        
        def three_digits(three_digit_num):
            hundreds = three_digit_num // 100
            remainder = three_digit_num % 100
            if hundreds and remainder:
                return one_digit[hundreds] + ' Hundred ' + two_digits(remainder) 
            elif not hundreds and remainder: 
                return two_digits(remainder)
            elif hundreds and not remainder:
                return one_digit[hundreds] + ' Hundred'
        
        if not num:
            return 'Zero'

        num_as_words = ''

        # break down the number by sections of hundreds, a.k.a 3 digits
        # 10,000,000 hundreds
        billions = num // 1000000000
        if billions:
            num_as_words = three_digits(billions) + ' Billion '
            num -= billions * 1000000000

        # 10,000 hundreds
        millions = num // 1000000
        if millions:
            num_as_words += three_digits(millions) + ' Million '
            num -= millions * 1000000

        # 10 hundreds
        thousands = num // 1000
        if thousands:
            num_as_words += three_digits(thousands) + ' Thousand '
            num -= thousands * 1000

        # num is now 999 or less
        if num:
            num_as_words += three_digits(num)

        strip_extra_spaces = num_as_words.strip()
        return strip_extra_spaces

tests = [
    dict(
        input=0,
        output="Zero"),
    dict(
        input=1000,
        output="One Thousand"),
    dict(
        input=1234567,
        output="One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
]

for test in tests:
    new_solution = Solution()
    assert new_solution.numberToWords(test['input']) == test['output']

# Runtime: 40 ms, faster than 28.58% of Python3 online submissions for Integer to English Words.
# Memory Usage: 13.8 MB, less than 68.78% of Python3 online submissions for Integer to English Words.
        