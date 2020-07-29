
# Imagine that you are a project manager. You have a number of developers in your team, and they report on different days they are working on. We want to calculate the number of days on which at least one developer is working.

# For example, let’s say you have 3 developers: A, B and C. They report the following working schedule:
# Developer A: day 4 - 6 (You can think of it as Thursday through Saturday)
# Developer B: day 1 and 5 (Tuesday and Saturday)
# Developer C: day 0 - 1 and 5 - 6 (Monday, Tuesday, Saturday and Sunday)

# Visually on a schedule, this would look like:
#     0  1  2  3  4  5  6 ... N
# A               1  1  1
# B      1           1
# C   1  1           1  1 
from typing import List

# Time: # employes * # max_session
# Space: however max days



def days_worked(employee_data: List[tuple]) -> int:
    counter = 0

    for start, end in employee_data:
        if start <= counter:
            if end > counter:
                counter = end
        if start > counter:
            days = end - start
            counter += days
            
    # starting at 0 index, so must add 1 at the end if there is a 0
    print(f'counter + 1: {counter + 1}')
    return counter + 1

input = [ 
    [ 
        [ 4, 6 ] 
    ], 
    [
        [ 1, 1 ], [ 5, 5 ] 
    ], 
    [
        [ 0, 1 ], [ 5, 6 ]
    ] 
]

sorted_input = [ [ 0, 1 ], [ 1, 1 ], [ 4, 6 ], [ 5, 5 ], [ 5, 6 ] ]
output = 5

assert days_worked(sorted_input) == output
# how many unique working days are there
# We want to calculate the number of days on which at least one developer is working.