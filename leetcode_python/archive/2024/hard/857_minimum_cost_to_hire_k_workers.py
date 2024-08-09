# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

# Anytime you see min or max, use a heap in Python.
# The idea here is that we want the K workers with the lowest wage-to-quality ratio because they will produce
# the lowest cost.

import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        # Sort workers by wage-to-quality ratio
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
      
        min_cost = float('inf')
        total_quality = 0
        # We're going to use heapq, which is a min heap, but since we'll be adding -quality values
        # it'll operate as a max heap for us
        max_heap = []
      
        for ratio, quality in workers:
            total_quality += quality
            heapq.heappush(max_heap, -quality)
            
            if len(max_heap) > k:
                # Remove highest quality worker from the heap and the total_quality_score

                # Example: highest quality worker is 10, but is represented in our heap as -10
                # You can do this one of two ways:
                # 1) Add the quality of the removed worker (which is actually negative), so
                # it reduces the total quality
                total_quality += heapq.heappop(max_heap)  
                # total_quality += -10
                # 2) Subtract the quality of the removed worker since it's stored as a negative value
                # total_quality -= -heapq.heappop(max_heap)
                # total_quality -= -(-10) => total_quality -= 10
                

            if len(max_heap) == k:
                # With workers sorted by their wage-to-quality ratio, the current worker's ratio becomes key for calculating the group's total cost.
                # It sets the pay rate, ensuring proportional pay across the board. Multiplying by total_quality adjusts this rate for each worker's quality.
                # This step checks if hiring these k workers is our best bet so far, updating min_cost if it beats previous options.
                min_cost = min(min_cost, ratio * total_quality)

      
        return min_cost

# Greedy algorithms make the locally optimal choice at each stage with the hope of finding a global optimum. 
# In this case, the "greedy" part comes from selecting workers with the lowest wage-to-quality ratio first, 
# under the assumption that hiring these workers will lead to the minimum total cost.
