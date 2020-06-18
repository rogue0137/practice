# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # you will need three pointers; you will have to create a dummy node for the third pointer
        pointer_for_l1 = l1
        pointer_for_l2 = l2
        dummy_node = ListNode()
        
        # this will be the pointer for the dummy node, we'll build on top of this
        curr = dummy_node
        carry = 0

        # you want to ensure that at least one of the pointers will have a value
        # if one of them has a value, continue to loop
        while pointer_for_l1 != None or pointer_for_l2 != None:
            # because your while loop looks for the current pointer, not next, compare to the pointer when looking for val
            if pointer_for_l1 != None:
                x = pointer_for_l1.val
            else:
                x = 0
            if pointer_for_l2 != None:
                y = pointer_for_l2.val
            else:
                y = 0
            
            sum = x + y + carry
            modulus = sum % 10
            carry = sum // 10
            
            # ADD NODE TO CREATED LISTNODE
            curr.next = ListNode(val=modulus)
            
            # MOVE POINTERS
            # move pointer 3
            curr = curr.next
            # move pointer 1: only try to advance if not None
            if pointer_for_l1 != None:
                pointer_for_l1 = pointer_for_l1.next
            # move pointer 2: only try to advance if not None
            if pointer_for_l2 != None:
                pointer_for_l2 = pointer_for_l2.next

        # when you exit the while loop, carry may still have a value
        # if it has a value, you have to add a node
        if carry > 0:
            curr.next = ListNode(val=carry)

        # you want to return what you've linked to the dummy node as a new linked list, but exclude the dummy node, so use next
        return dummy_node.next

# BELOW w/out any comments
# Runtime: 64 ms, faster than 95.10% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14 MB, less than 9.89% of Python3 online submissions for Add Two Numbers.