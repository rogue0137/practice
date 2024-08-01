# Weekly Learnings: July29toAugust2

## Patterns

## Tracking Weak Spots

## Learnings

Summarize this:

How to call a function directly after class initialization:

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
Summarize this:

RE Overflow: Python does not have built-in limits for integers, but for floating-point operations, you can compare against sys.float_info.max.

Summarize this:

The line max_heap = [-num for num in list_of_ints[:k]] is used to initialize a max heap from the first (k) elements of the list, but it does so by negating the numbers. This might seem counterintuitive at first glance, especially since Python's heapq module provides a min heap functionality out of the box, not a max heap. The reason for this approach is rooted in the limitations of the available heap implementation and the desired outcome of tracking the (k) largest numbers.

Understanding the Reasoning
Python's Heapq Module: The heapq module in Python implements a min heap, meaning that the smallest element gets pushed to the index position 0. However, for this problem, we are interested in keeping track of the (k) largest numbers, which naturally suggests the need for a max heap.
Negating Numbers: By negating the numbers before inserting them into the heap, we essentially invert their order. This means that the largest number (which becomes the smallest when negated) will be considered the "smallest" by the min heap logic and thus will be placed at the top of the heap. Conversely, the smallest positive number (which becomes the largest negative number) will be at the bottom of the heap.
Effectively Creating a Max Heap: Through this negation, we simulate a max heap behavior using Python's min heap functionality. When we pop elements from this heap, we get them in descending order of their original positive values, which aligns with our goal of tracking the (k) largest numbers.
Simplifying Retrieval: When retrieving the numbers from the heap for calculating the product, we negate them again to convert them back to their original positive values. This double negation (-(-num)) effectively cancels out, returning the numbers to their original state.
Example Clarification
Consider a list [10, 20, 30], and let's say we want to track the 2 largest numbers using a heap. Without negation, inserting these into a min heap would result in [10, 20] with 10 at the top because it's the smallest. However, by negating the numbers ([-10, -20, -30]), inserting them into the min heap results in [-30, -20] with -30 at the top, which corresponds to 30 being the largest number in the original list. This way, we maintain the largest numbers at the top of the heap, achieving the desired max heap behavior.

In summary, negating the numbers allows us to leverage Python's built-in min heap functionality to efficiently track the (k) largest numbers in a list, which is crucial for solving the problem without sorting.

### New and Reviewd Weekly Problems
- [apple_stocks](interview_cake/2024/apple_stocks.py)
- [cafe_order_checker](interview_cake/2024/cafe_order_checker.py)
- [inflight_entertainment](interview_cake/2024/inflight_entertainment.py)
- [merge_calendar_tool](interview_cake/2024/merge_calendar_tool.py)
- [merge_sorted_lists](interview_cake/2024/merge_sorted_lists.py)
- [palindrome_permutation](interview_cake/2024/palindrome_permutation.py)
- [reverse_list_of_characters](interview_cake/2024/reverse_list_of_characters.py)
- [reverse_words](interview_cake/2024/reverse_words.py)
