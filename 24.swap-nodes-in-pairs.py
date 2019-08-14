#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        secondHead = self.swapPairs(head.next.next)
        newHead = head.next
        newHead.next = head
        head.next = secondHead
        return newHead
