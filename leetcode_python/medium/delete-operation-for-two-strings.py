# 583. Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        return missing_chars

tests = [
    dict(word1="sea",word2="eat",output=2),
    dict(word1="sea",word2="ate",output=4)
]

for test in tests:
    solution = Solution()
    print(solution.minDistance(test['word1'],test['word2']))
    assert solution.minDistance(test['word1'],test['word2']) == test['output']