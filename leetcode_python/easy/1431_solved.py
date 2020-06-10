# 1431. Kids With the Greatest Number of Candies
# SOLVED?
# URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        most_candies = max(candies)
        for index, kids_candies in enumerate(candies):
            with_extra_candies = kids_candies + extra_candies
            if with_extra_candies >= most_candies:
                candies[index] = True
            else:
                candies[index] = False
        return candies
# Runtime: 60 ms, faster than 12.92% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.8 MB, less than 70.06% of Python3 online submissions for Kids With the Greatest Number of Candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extra_candies: int) -> List[bool]:
        most_candies = max(candies)
        is_cool_kid = []
        for kids_candies in candies:
            with_extra_candies = kids_candies + extra_candies
            if with_extra_candies >= most_candies:
                is_cool_kid.append(True)
            else:
                 is_cool_kid.append(False)
        return is_cool_kid

# apparently enumerate is a heavy operation; not using the original list also uses less memory
# Runtime: 20 ms, faster than 99.98% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.8 MB, less than 75.97% of Python3 online submissions for Kids With the Greatest Number of Candies.