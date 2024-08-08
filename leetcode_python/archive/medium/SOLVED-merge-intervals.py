# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        len_arr = len(intervals)
        if len_arr == 0:
            return []

        # new array
        merged_intervals = []

        # always make sure they're sorted
        # it'll help with loop iteration

        sorted_intervals = sorted(intervals)
        start, end = sorted_intervals[0]

        # iterate through array, start at index 1
        for i in range(1, len_arr):
            curr_start, curr_end = sorted_intervals[i]
            if curr_start <= end:
                # do NOT update start
                # update end
                end = max(curr_end, end)
            
            else: # curr_start > end
                # append(start, end)
                merged_intervals.append([start, end])
                # update_start
                start = curr_start
                # update_end
                end = curr_end
        # outside loop
        # append(start, end)
        merged_intervals.append([start, end])

        return merged_intervals

# Runtime: 72 ms, faster than 99.96% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.7 MB, less than 16.05% of Python3 online submissions for Merge Intervals.

# ROUND 1
    # start: 1
    # end: 3
    # curr_start: 2
    # curr_end: 6
    # curr_start vs. end
        # 2 < 3
        # current_start is included in end
        # do NOT update start
        # check end vs. curr_end, reset end to max of two
        # end = max(curr_end, end)
# ROUND 2
    # start: 1
    # end: 6
    # curr_start: 8
    # curr_end: 10
    # curr_start vs. end
        # 8 > 6: curr start is bigger than end
        # append previous 
            # append(start, end) --> [1, 6]
        # update start and end
        # start = curr_start
        # end = curr_end
# ROUND 3
    # start = 8
    # end = 10
    # curr_start = 15
    # curr_end = 18
    # curr_start vs. end
        # 15 > 10: curr start is bigger than end
        # append prev
            # append(start, end) --> [1,6], [8, 10]
            # update start and end
            # start = curr_start --> 15
            # end = curr_end --> 18

# OUTSIDE LOOP
# add last start end
# append(start, end) --> [1, 6], [8, 10], [15, 18]
