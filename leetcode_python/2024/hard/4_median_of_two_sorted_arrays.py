# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List

# This one is a doozy. The comments immediately below are me asking Phind (using Claude) to summarize
# code comments in a way that makes more sense and provide an example. 

# Binary search approach to find the median
# We aim to partition both arrays into left and right halves
# such that all elements in the left half are <= all elements in the right half
# The partition point will give us the median

# Key ideas:
# 1. We perform binary search on the smaller array (nums1) to minimize operations
# 2. For each midpoint in nums1, we calculate a complementary point in nums2
# 3. We compare elements around these points to ensure correct partitioning
# 4. We adjust our search based on these comparisons until we find the correct partition

# Example: 
# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 18, 19, 21, 25]
# We search for a partition in nums1 and calculate the corresponding partition in nums2
# that together form the correct median partition of the merged array

# The goal is to find:
# max(nums1[left_partition]) <= min(nums2[right_partition]) AND
# max(nums2[left_partition]) <= min(nums1[right_partition])

# When this condition is met, we've found our median partition

# EXAMPLE:

# ITERATION 1

# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 18, 19, 21, 25]

# start = 0, end = 5
# midpoint = 2
# complementMidpoint = 3

# Partition:
# nums1: [1, 3 | 8, 9, 15]
# nums2: [7, 11, 18 | 19, 21, 25]

# Values:
# maxValueBeforeMidpoint = nums1[1] = 3
# minValueAfterMidpoint = nums1[2] = 8
# maxValueBeforeComplementMidpoint = nums2[2] = 18
# minValueAfterComplementMidpoint = nums2[3] = 19

# Compare: 
# 3 <= 19 (maxValueBeforeMidpoint <= minValueAfterComplementMidpoint) : True
# 18 <= 8 (maxValueBeforeComplementMidpoint <= minValueAfterMidpoint) : False
# Result: Not valid
# Action: Move start to midpoint + 1


# ITERATION 2:
# nums1 = [1, 3, 8, 9, 15]
# nums2 = [7, 11, 18, 19, 21, 25]

# start = 3, end = 5
# midpoint = 4
# complementMidpoint = 1

# Partition:
# nums1: [1, 3, 8, 9 | 15]
# nums2: [7 | 11, 18, 19, 21, 25]

# Values:
# maxValueBeforeMidpoint = nums1[3] = 9
# minValueAfterMidpoint = nums1[4] = 15
# maxValueBeforeComplementMidpoint = nums2[0] = 7
# minValueAfterComplementMidpoint = nums2[1] = 11

# Compare:
# 9 <= 11 (maxValueBeforeMidpoint <= minValueAfterComplementMidpoint) : True
# 7 <= 15 (maxValueBeforeComplementMidpoint <= minValueAfterMidpoint) : True
# Result: Valid
# Action: Found the correct partition
# Total elements: 11 (odd)
# Median: max(maxValueBeforeMidpoint, maxValueBeforeComplementMidpoint) = max(9, 7) = 9



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Swap nums1 and nums2
        
        # Lengths of the input arrays
        len_of_nums1, len_of_nums2 = len(nums1), len(nums2)
        
        # Initialize pointers for binary search within nums1
        start, end = 0, len_of_nums1

        # We're going to split up the arrays until we find the point where we can
        # get half of the merged, sorted array. We only need half (+1?) of the total arrayto understand the median.
        # To understand this, we'll have to figure out where the actual midpoint is
        # on the smaller array (renamed to nums1 above)
        # We need to compare values to see if we are truly sorted
        # Example: nums1 = [1, 6, 7, 8] and nums = [2, 3]
        while start <= end:
            # Calculate the midpoint for nums1 and the complement midpoint for nums2
            midpoint = (start + end) // 2
            complementMidpoint = (len_of_nums1 + len_of_nums2 + 1) // 2 - midpoint

            # Find elements around the midpoints
            maxValueBeforeMidpoint = float('-inf') if midpoint == 0 else nums1[midpoint - 1]
            minValueAfterMidpoint = float('inf') if midpoint == len_of_nums1 else nums1[midpoint]
            maxValueBeforeComplementMidpoint = float('-inf') if complementMidpoint == 0 else nums2[complementMidpoint - 1]
            minValueAfterComplementMidpoint = float('inf') if complementMidpoint == len_of_nums2 else nums2[complementMidpoint]

            # Check if the current partition is valid (max left <= min right)
            if maxValueBeforeMidpoint <= minValueAfterComplementMidpoint and maxValueBeforeComplementMidpoint <= minValueAfterMidpoint:
                # If total length is even, median is the average of the two middle numbers
                if (len_of_nums1 + len_of_nums2) % 2 == 0:
                    largestValueOnLeftSide = max(maxValueBeforeMidpoint, maxValueBeforeComplementMidpoint)
                    smallestValueOnRightSide = min(minValueAfterMidpoint, minValueAfterComplementMidpoint)
                    median = (largestValueOnLeftSide + smallestValueOnRightSide) / 2
                    return median
                # If total length is odd, median is the larger of the two numbers on the left side
                else:
                    # note how this is the same as largestValueOnLeftSide above
                    median = max(maxValueBeforeMidpoint, maxValueBeforeComplementMidpoint)
                    return median
            # Adjust the binary search range based on the comparison
            elif maxValueBeforeMidpoint > minValueAfterComplementMidpoint:
                end = midpoint - 1  # Move the midpoint towards the smaller values in nums1
            else:
                start = midpoint + 1  # Move the midpoint towards the larger values in nums1
