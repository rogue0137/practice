# 160. Intersection of Two Linked Lists
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solved? 
# Write a program to find the node at which the intersection of two singly linked lists begins.

# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Two pointers
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        while (p1 != p2) and (p1 or p2):
            if p1 == None:
                p1 = headB
            if p2 == None:
                p2 = headA
            if p1 == p2: 
                return p1
            p1 = p1.next
            p2 = p2.next
                
        return p1
# Runtime: 228 ms, faster than 10.92% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 29 MB, less than 78.41% of Python3 online submissions for Intersection of Two Linked Lists.

# Brute force, still exceeds time limit, python may not be fast enough for this approach to meet leetcode time limit
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        p1_values = []
        while p1:
            p1_values.append(p1)
            p1 = p1.next
        while p2:
            if p2 in p1_values:
                return p2
            p2 = p2.next
        return None
