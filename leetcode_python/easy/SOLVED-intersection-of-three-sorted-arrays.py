# 1213. Intersection of Three Sorted Arrays
# https://leetcode.com/problems/intersection-of-three-sorted-arrays/

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        intersection = []
        for num in arr1:
            if num in arr2:
                if num in arr3:
                    intersection.append(num)
        return intersection 

# Runtime: 236 ms, faster than 13.14% of Python3 online submissions for Intersection of Three Sorted Arrays.
# Memory Usage: 13.9 MB, less than 79.77% of Python3 online submissions for Intersection of Three Sorted Arrays.

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        set_intersection = set(arr1) & set(arr2) & set(arr3)
        sorted_intersection = sorted(set_intersection)
        set_as_list = list(sorted_intersection)
        return set_as_list

# use sets!
# Runtime: 84 ms, faster than 77.75% of Python3 online submissions for Intersection of Three Sorted Arrays.
# Memory Usage: 13.8 MB, less than 94.46% of Python3 online submissions for Intersection of Three Sorted Arrays.