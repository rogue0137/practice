# 15. 3Sum
# https://leetcode.com/problems/3sum/

# Hash set
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        found = set()
        for i, val1 in enumerate(nums):
            print('--- SETTING VAL 1')
            print(f'i: {i}, val1: {val1}')
            seen = set()
            for j, val2 in enumerate(nums[i+1:]):
                print(f'j: {j}, val2: {val2}')
                complement = -val1 - val2
                print(f'complement: {complement}')
                if complement in seen:
                    print('--complement seen---')
                    min_val = min((val1, val2, complement))
                    print(f'min_val: {min_val}')
                    max_val = max((val1, val2, complement))
                    print(f'max_val: {max_val}')
                    print(f'found: {found}')
                    if (min_val, max_val) not in found:
                        print('min max not in found')
                        print('adding min and max to found')
                        found.add((min_val, max_val))
                        print(f'ADD to found: {found}')
                        print(f'appending result: {val1}, {val2}, {complement}')
                        res.append([val1, val2, complement])
                print(f'add val2 to seen: {val2}')
                seen.add(val2)
                print(f'seen: {seen}')
        return res