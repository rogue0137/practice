# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# BRUTE FORCE
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # new array to store all values the nodes of all lists
        self.nodes = []

        # head = set this so you can return it later
        # point = you're going to use this to build the new LinkedList
        # these need to be equated here to each other
        head = point = ListNode(0)

        # for each linkedList in the array of linkedLists
        for l in lists:
            while l:
                self.nodes.append(l.val)
                # this part enables you to iterate through the linkedList until its done
                l = l.next

        # sort your array using built in sort, why make it hard on yourself?
        # now, go through it and link all nodes
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next 

# Runtime: 104 ms, faster than 86.15% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18 MB, less than 32.63% of Python3 online submissions for Merge k Sorted Lists.

# TRY THIS LATER: https://dbader.org/blog/priority-queues-in-python