# 237. Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

# Runtime: 56 ms, faster than 5.58% of Python3 online submissions for Delete Node in a Linked List.
# Memory Usage: 14.1 MB, less than 79.41% of Python3 online submissions for Delete Node in a Linked List.