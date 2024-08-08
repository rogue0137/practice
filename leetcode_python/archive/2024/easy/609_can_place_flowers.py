# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/description/


# Scenarios where we can plant a new flower. 
# 
# The current plot is empty AND one of the following:
#   1) either side of the curr_plot do not have flowers
#   2) the plot is in the first index and the right side of the plot does not have a flower
#   3) the plot is in the last index and the left side of the plot does not have a flower

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Immediately return True if no flowers need to be planted
        if n == 0:
            return True

        new_flowers = 0
    
        for i in range(len(flowerbed)):
            curr_plot = flowerbed[i]

            empty_curr_plot = curr_plot == 0
            empty_prev_plot = i == 0 or flowerbed[i-1] == 0
            empty_next_plot = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if empty_curr_plot and empty_prev_plot and empty_next_plot:
                flowerbed[i] = 1
                new_flowers += 1
                
                if new_flowers == n:
                    return True
        
        return False

# Greedy algorithms make the locally optimal choice at each stage with the hope of finding a global optimum. 
# In this case, the "greedy" part comes from choosing to plant a flower whenever it's immediately possible to 
# do so without checking future possibilities. This strategy assumes that planting a flower as soon as you 
# find a valid spot will lead to the maximum number of flowers being planted, which holds true under the 
# constraints given by the problem.
