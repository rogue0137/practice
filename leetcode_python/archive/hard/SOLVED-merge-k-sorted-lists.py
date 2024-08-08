# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TALK ABOUT PASS BY REFERENCE AND TALK BY VALUE

# BRUTE FORCE
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # new array to store all values the nodes of all lists
        self.nodes = []

        # real = set this so you can return it later
        # dummy = you're going to use this to build the new LinkedList
        # these need to be equated here to each other
        # See pass by reference vs. pass by value
        # https://stackoverflow.com/questions/373419/whats-the-difference-between-passing-by-reference-vs-passing-by-value
        real = dummy = ListNode(0)

        # for each linkedList in the array of linkedLists
        for l in lists:
            while l:
                self.nodes.append(l.val)
                # this part enables you to iterate through the linkedList until its done
                l = l.next

        # sort your array using built in sort, why make it hard on yourself?
        # now, go through it and link all nodes
        for x in sorted(self.nodes):
            dummy.next = ListNode(x)
            dummy = dummy.next
        return real.next 

# Runtime: 104 ms, faster than 86.15% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18 MB, less than 32.63% of Python3 online submissions for Merge k Sorted Lists.

# USING HEAP
import heapq
# heap is a way to implement a priority queue
# https://en.wikipedia.org/wiki/Heap_(data_structure)
# https://realpython.com/python-heapq-module/

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for l in lists:
            while l:
                heap.append(l.val)
                l = l.next

        heapq.heapify(heap)
        real = dummy = ListNode(0)
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            dummy.next = node
            # setting up for the next iteration
            dummy = dummy.next

        return real.next

# Runtime: 144 ms, faster than 51.01% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18 MB, less than 29.79% of Python3 online submissions for Merge k Sorted Lists.

# Input: 
# [[1,4,5],[1,3,4],[2,6]]
# heap: [1, 1, 2, 4, 3, 4, 5, 6]
# val: 1
# NEXT: ListNode{val: 0, next: ListNode{val: 1, next: None}}
# dummy = node: ListNode{val: 1, next: None}
# val: 1
# NEXT: ListNode{val: 1, next: ListNode{val: 1, next: None}}
# dummy = node: ListNode{val: 1, next: None}
# val: 2
# NEXT: ListNode{val: 1, next: ListNode{val: 2, next: None}}
# dummy = node: ListNode{val: 2, next: None}
# val: 3
# NEXT: ListNode{val: 2, next: ListNode{val: 3, next: None}}
# dummy = node: ListNode{val: 3, next: None}
# val: 4
# NEXT: ListNode{val: 3, next: ListNode{val: 4, next: None}}
# dummy = node: ListNode{val: 4, next: None}
# val: 4
# NEXT: ListNode{val: 4, next: ListNode{val: 4, next: None}}
# dummy = node: ListNode{val: 4, next: None}
# val: 5
# NEXT: ListNode{val: 4, next: ListNode{val: 5, next: None}}
# dummy = node: ListNode{val: 5, next: None}
# val: 6
# NEXT: ListNode{val: 5, next: ListNode{val: 6, next: None}}
# dummy = node: ListNode{val: 6, next: None}
# head: ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}}}}


# USING PRIORITY QUEUE IN PYTHON
from queue import PriorityQueue
# SEE: https://dbader.org/blog/priority-queues-in-python

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        real = dummy = ListNode(0)
        Q = PriorityQueue()
        for l in lists:
            while l:
                Q.put((l.val))
                l = l.next
        while not Q.empty():
            val = Q.get()
            node = ListNode(val)
            dummy.next = node
            dummy = dummy.next
        return real.next

# Runtime: 196 ms, faster than 29.18% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18.1 MB, less than 21.33% of Python3 online submissions for Merge k Sorted Lists.