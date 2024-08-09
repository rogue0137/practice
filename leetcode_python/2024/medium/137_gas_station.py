# https://leetcode.com/problems/gas-station/description/
# related google drawing:
# https://docs.google.com/drawings/d/1UPUB4rgKcUMyr78abmfc9WD7H5rxFTpBt3hc-1syz5A/edit

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Do we have enough gas to cover costs? 
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_cost > total_gas: # Nope
            return -1 
        
        # Greedy values
        # Initialize variables for tracking gas balance and starting point
        cummulative_gas = 0
        starting_point = 0
        debt = 0

        # Time to loop!
        for i in range(len(gas)):
            cummulative_gas += gas[i] - cost[i]
            
            # If cummulative_gas becomes negative:
            # 1. update starting_point
            # 2. add to debt (because you have to pay for a new starting_point)
            # 3. reset cummulative_gas to 0 since you have a new starting point
            if cummulative_gas < 0:
                starting_point = (i + 1) % len(gas)
                debt += cummulative_gas
                cummulative_gas = 0

        # Even though we checked if total_gas could cover total_cost at the beginning of this problem,
        # we do not know the distribution of costs and gas. 
        # By adding debt to the final cummulative_gas (which represents the net gas remaining after a 
        # full loop from the proposed starting point), you're essentially checking if starting from the
        # identified point allows you to not only complete the circuit but also overcome any accumulated
        # deficits. 
        # If cummulative_gas + debt >= 0, it means you have enough gas to compensate for any deficits 
        # encountered along the way, validating the starting point.
        if cummulative_gas + debt >= 0:
            return starting_point
        else:
            return -1

            




        