# 206. Reverse Linked List
# URL: https://leetcode.com/problems/reverse-linked-list/
# SOLVED? Yes, iterative; still working through recursive
# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative Solution
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # start with the head
        cur = head
        # you'll need a prev_node, but because the first node doesn't have it, you'll set this to None
        prev_node = None
        print(f'starting cur: {cur}')
        print(f'starting prev_node: {prev_node}')
        # when cur eventually becomes None, you want to exist the loop
        while cur:
            print('LOOPING')
            # you need access to the next node so you can eventually make it the current node
            next_node = cur.next
            print(f'next node: {next_node}')
            # start reversing, after pointer points to prev point (aka opposite direction)
            cur.next = prev_node
            print(f'cur.next: {cur.next}')
            # previous node gets updated to the node you started on
            prev_node = cur
            print(f'prev_node: {prev_node}')
            # the current node gets updated to the original node.next
            cur = next_node
            print(f'updated cur: {cur}')
        # you want to return the prev_node, not the head, because the head is still pointed to the right way, but your new linkedList's head is at prev_node
        print(f'head: {head}')
        print(f'prev_node: {prev_node}')
        return prev_node

# PRINT STATEMENTS
# starting cur: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}}
# starting prev_node: None
# LOOPING
# next node: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# cur.next: None
# prev_node: ListNode{val: 1, next: None}
# updated cur: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
# LOOPING
# next node: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# cur.next: ListNode{val: 1, next: None}
# prev_node: ListNode{val: 2, next: ListNode{val: 1, next: None}}
# updated cur: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
# LOOPING
# next node: ListNode{val: 4, next: ListNode{val: 5, next: None}}
# cur.next: ListNode{val: 2, next: ListNode{val: 1, next: None}}
# prev_node: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
# updated cur: ListNode{val: 4, next: ListNode{val: 5, next: None}}
# LOOPING
# next node: ListNode{val: 5, next: None}
# cur.next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}
# prev_node: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
# updated cur: ListNode{val: 5, next: None}
# LOOPING
# next node: None
# cur.next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}
# prev_node: ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}
# updated cur: None
# head: ListNode{val: 1, next: None}
# prev_node: ListNode{val: 5, next: ListNode{val: 4, next: ListNode{val: 3, next: ListNode{val: 2, next: ListNode{val: 1, next: None}}}}}

# Below is without all the print statemetns and explanations:
# Runtime: 28 ms, faster than 95.93% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.3 MB, less than 59.70% of Python3 online submissions for Reverse Linked List.


# Recursive Solution
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            print('HERE')
            return head
        print('before next')
        next = self.reverseList(head.next)
        print('next')
        head.next.next = head
        print(f'head.next.next = {head.next.next}')
        head.next = None
        print(f'head.next = {head.next}')
        return next
# Below is without all the print statemetns and explanations:
# Recursive solutoin is SLOW and suboptimal memorywise
# Runtime: 64 ms, faster than 6.17% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 18.5 MB, less than 14.08% of Python3 online submissions for Reverse Linked List.