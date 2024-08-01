# Weekly Learnings: July29toAugust2

![gorilla on computer](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnY2Mmg4dHloNGlydWNsZ3Y3bzI2dXB4bGRyYnd1cDRrbHowYzY1dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QNFhOolVeCzPQ2Mx85/giphy.gif)
## New and Reviewed Weekly Problems
- [apple_stocks](interview_cake/2024/July28toAugust2/apple_stocks.py)
- [cafe_order_checker](interview_cake/2024/July28toAugust2/cafe_order_checker.py)
- [inflight_entertainment](interview_cake/2024/July28toAugust2/inflight_entertainment.py)
- [merge_calendar_tool](interview_cake/2024/July28toAugust2/merge_calendar_tool.py)
- [merge_sorted_lists](interview_cake/2024/July28toAugust2/merge_sorted_lists.py)
- [palindrome_permutation](interview_cake/2024/July28toAugust2/palindrome_permutation.py)
- [product_of_all_other_numbers](interview_cake/2024/July28toAugust2/reverse_list_of_characters.py)
- [reverse_list_of_characters](interview_cake/2024/July28toAugust2/reverse_list_of_characters.py)
- [reverse_words](interview_cake/2024/July28toAugust2/reverse_words.py)
- [word_cloud](interview_cake/2024/July28toAugust2/word_cloud.py)

## Patterns

### Merging Times and Saving Space

If you want to "save space", you must:
- Keep track of the index, e.g. `i = 0`
- Then, loop through the entire list of tuples, starting on the second item
```Python
for second_meeting_index in range(1, len(meetings)):
```
- If a meeting overlaps, you will replace the current tuple at that index with an updated tuple; you will not update `i` because you'll want to check if the next meeting can also be merged in
- If a meeting doesn't overlap, you won't replace it, but you'll increment the index so that you don't update an index you're not supposed to
- Whatever `i` is at the end, that's the only # of entries in the array you want to take, so you'll have to update it to get rid of data you don't need
```Python
    # Example of variables at this point: 
    # i = 2
    # [(1, 4), (5, 8), (9, 10), (6, 8), (9, 10)]
    # We need to remove (6, 8), (9, 10) from the list, so we use `[i+1:]` since we only need up to [i]
    del meetings[i+1:]
```

### Find K Largest/Smallest Numbers

Largest
```Python
import heapq

def find_k_largest_numbers(nums, k):
    # Create a min heap with the first k numbers
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    
    # Iterate over the rest of the numbers
    for num in nums[k:]:
        # If the current number is greater than the smallest in the heap,
        # replace the smallest with the current number
        if num > min_heap[0]:
            heapq.heappushpop(min_heap, num)
    
    # At this point, min_heap contains the k largest numbers
    return sorted(min_heap, reverse=True)  # Sorting to get them in descending order

list_of_ints = [4, 2, 9, 6, 23, 12]
k = 3
k_largest_numbers = find_k_largest_numbers(list_of_ints, k) # 23, 12, 9
```

Smallest
```Python
# basically, use built-in heapq.nsmallest()
import heapq

list_of_ints = [4, 2, 9, 6, 23, 12]

# Find the smallest k numbers
k = 3
smallest_k_numbers = heapq.nsmallest(k, list_of_ints)
# Expected output: [2, 4, 6]

```


## Tracking Weak Spots

## Learnings

- All lists in Python are dynamic arrays. Python doesn't have fixed-sized arrays.

- Strings are iterable in Python.

```Python
for index, char in enumerate(input_string):
```
- Creating new lists the size of an old list is easy:
```Python
new_list = [None] * len(old_list)
```
- Duh, Python has `isalpha()`.

```Python
# Example
char_one = 'e'
char_two = 1
char_one.isalpha() # True
char_two.isalpha() # False
```
- This is how you interact forwards and backwards on a list:
```Python
# forwards
for i in range(len_of_int_list):
    ...
# backwards
for i in range(len_of_int_list - 1, -1, -1):
    ...
# reminder for range: range(start, stop, step)
```
- How to call a function directly after class initialization:

```Python
class WordCloudData(object):

    def __init__(self, input_string):

        self.input_string = input_string
        self.words_to_counts = {}
        
        # THIS HERE
        self.count_words()
        
    def deal_with_punctuation(self, prev_word):
        ...
    
    def count_words(self:)
        ...
```
- Python does not have built-in limits for integers, so they cannot Overflow. If you are doing floating-point operations, you can compare against sys.float_info.max to make sure you do not overflow.
```Python
import sys

# Define two large floating-point numbers close to sys.float_info.max
num_one = 1.8e308  # A large number close to the max float value
num_two = 2.0      # Another number we want to multiply with num_one

# Check if the product would exceed sys.float_info.max
if num_one * num_two <= sys.float_info.max:
    result = num_one * num_two
    print(f"The multiplication result is: {result}")
else:
    print("Multiplication would cause an overflow.")
```
- Python's heapq module implements a min heap.
- Reminder: Min heap pushes the smallest number to the top. 
- If you want to turn it into a max heap, you could do it like so:
```Python
import heapq

# Turn every number the opposite of what it is. Positive numbers will become
# negative. Thus a more positive number will be higher up the heap. 
max_heap = [-num for num in list_of_ints]
heapq.heapify(max_heap)

# However, when returning the largest number, you need to remember to switch the number back to whatever it was originally
biggest_number_after_switch = max_heap[0]
original_number = -biggest_number_after_switch
```


