# Weekly Learnings: August12toAugust17

## New and Reviewed Weekly Problems

### Interview Cake
- [find_rotation_point.py](find_rotation_point.py)
- [find_duplicate.py](find_duplicate.py)

### Leetcode Binary Search Practice
- [35_search_insert_position](../../../leetcode_python/2024/easy/35_search_insert_position.py)
- [hard/4_median_of_two_sorted_arrays](../../../leetcode_python/2024/hard/4_median_of_two_sorted_arrays.py)
- [33_search_rotated_sorted_array.py](../../../leetcode_python/2024/medium/33_search_rotated_sorted_array.py)

### Leetcode Binary Search Tree Practice
- []
## Tracking Weak Spots 

I need to go back to basics.

### Binary Search Trees

- I keep trying to use stacks and queues when they are unnecessary for solving the problem. **Sometimes you really can just use a secondary function and pointers**.

### Graphs
- I feel more comfortable using recursive functions for DFS and BFS. Goal is to get as comfortable with iterative approaches.

### Binary Search
- Because binary search is generally for sorted numbers, instead of using pointer terms `left` and `right`, you can also use `low` and `high`
- When we reset a `left/low` or a `right/high`, we must always be sure to `add/subtract` respectively from the `mid`. Here's an example:
```Python
n = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

# first low, high
low, high = 0, 9
# find midpoint
midpoint = (0 + 9) // 2 = 4
mid_number = n[4] = 16
# is mid_number higher or lower than target?
16 < 23
# because it is more, we have to move the low/left point higher
# we have to ADD one because we know it's not at mid point
low = midpoint + 1
```
- TLDR: using`mid - 1` and `mid + 1` in binary search algorithms is essential for avoiding infinite loops and correctly narrowing down the search space to efficiently find the target value or determine its absence
- This is a good overview that is helping me solve them Binary Search problems more easily:
```Python
# General properties of Binary Search:
    # left/low
    # right/high
    # while loop, usually <=, sometimes <
    # midpoint
    # reset low or high -/+
```
- However, sometimes we really will set to mid instead of mid +/- 1.

## To Do List

- [x] Redo find_rotation_point (binary search)

8/15
- [x] Solve highest_product_of_three but for 4 numbers
- [X] Spend time with Interview Cake Tree Problems
- [x] Redo find_duplicate (binary search)

8/16
- [ ] Do only easy greedy algo, binary search and binary search tree problems to make sure I understand the foundations

For next week?
- [ ] Redo binary search tree checker
- [ ] Redo find second largest element in binary search tree
- [ ] Read this editorial: https://leetcode.com/problems/find-the-duplicate-number/editorial/
- [ ] Solve [product_of_all_other_numbers](product_of_all_other_numbers.py) using division. Watchout for 0s!
- [ ] Solve highest_product_of_three, but for K numbers
- [ ] Solve [inflight_entertainment](inflight_entertainment.py) question #2 using dynamic programming. ( _Carry this TODO over until you get to the dynamic programming section._)
- [ ] Solve balanced_binary_tree with no help.
- [ ] Do a new leetcode binary search problem
- [ ] Redo merge_meeting_times (binary search, check that this is BS)
- [ ] Try another Leetcode Greedy Algo
- [ ] Need to practice creating a hash table without collisions from a class

## Patterns

### Binary Search
- **Basic** Binary Search: Typically uses "less than or equal to" (<=) to ensure the algorithm exhaustively searches the entire relevant portion of the array.
- **Boundary** Searches: May use "less than" (<) to better handle cases where the target is not found and to accurately identify insertion points or boundaries.

### Graphs

Ways to store graphs:
- Edge list
- Adjaceny list
- Adjacency matrix
DFS VS. BFS
- Depth first search uses stacks (pancakes)
- Breadth first search uses queues

## Learnings
- When working with perfect binary trees, you can get the count of the total nodes in the tree by taking the number of nodes on the last level, multiplying it by 2, and subtracting 1.
```Python
# This is how it starts out
n = (2 ^ h−1) ∗ 2 − 1
# YOu can reduce it to this
n = 2^h − 1
```

