# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

    # 1. access the length of the array
    # 2. final value -- DP here: we are "caching" a value and updating it
    # 3. intermediate value
    # 4. loop 
        # 5. within loop, max or min: MAX used below 
        # 6. you'll usually have at least two of these
        # 7. start resetting for the next loop
        # -- DP below: we are repeating a mathematical equation
        #    to find out answer
        # MAX 1
        # MAX 2

class Solution:
    def numDecodings(self, s: str) -> int:
        # 0. If there is any way for your string to be blank, hedge your bets
        if not s:
            return 0
        # 1. Access the length of the array
        len_s = len_s

        # 2. DP cache created here
        #    We are hosting values and updating updating them
        cache = [0 for _ in range(len_s + 1)]

        # 3. Set the first two values in the cache
        cache[0] = 1
        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        cache[1] = 0 if s[0] == '0' else 1

        # 4. Loop
        for i in range(2, len(cache)):
            # -- DP below: we are repeating a mathematical equation
            #    to find out answer
            # Check if successful single digit decode is possible.
            if s[i-1] != '0':
                cache[i] += cache[i-1]

            # Check if successful two digit decode is possible.
            two_digit = int(s[i-2 : i])
            if two_digit >= 10 and two_digit <= 26:
                cache[i] += cache[i-2]
        # 5. return the last value of the cache as the answer
        return cache[len_s]
