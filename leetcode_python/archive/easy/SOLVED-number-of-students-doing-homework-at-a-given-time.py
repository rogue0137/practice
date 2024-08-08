# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students_studying = 0
        for i in range(len(startTime)):
            start = startTime[i]
            end = endTime[i]
            if start <= queryTime and end >= queryTime:
                students_studying += 1
        return students_studying

# Runtime: 36 ms, faster than 83.05% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
# Memory Usage: 13.7 MB, less than 87.41% of Python3 online submissions for Number of Students Doing Homework at a Given Time.
