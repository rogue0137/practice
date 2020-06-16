# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c," ")
        paragraph.strip()
        split_paragraph = paragraph.lower().split(' ')
        print(split_paragraph)
        words_counter = dict()
        for word in split_paragraph:
            if word in banned:
                continue
            if words_counter.get(word):
                words_counter[word] += 1
            else:     
                words_counter[word] = 1
        k, v = '', 0
        for key, value in words_counter.items():
            if value > v:
                k, v = key, value
        return k