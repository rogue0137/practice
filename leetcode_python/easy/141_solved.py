# 141. Linked List Cycle
# LINK: https://leetcode.com/problems/linked-list-cycle/
# SOLVED? YES, idd not try using constant maemory


# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # if two pointers of different speeds ever meet, then there is a cycle
        first_pointer = head
        second_pointer = head
        while (second_pointer != None and second_pointer.next !=None):
            second_pointer = second_pointer.next.next;
            first_pointer = first_pointer.next;
            if second_pointer == first_pointer:
               return True
        return False

# Runtime: 88 ms, faster than 9.02% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17 MB, less than 19.57% of Python3 online submissions for Linked List Cycle.