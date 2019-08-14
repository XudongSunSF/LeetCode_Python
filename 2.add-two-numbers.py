#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = None
        head = result
        while True:
            if l1 is None and l2 is None:
                if carry != 0:
                    result.next = ListNode(carry)
                return head
            else:
                val1, val2 = 0, 0
                if l1 is not None:
                    val1 = l1.val
                    l1 = l1.next
                if l2 is not None:
                    val2 = l2.val
                    l2 = l2.next

                tmp = val1 + val2 + carry
                if result is None:
                    result = ListNode(tmp % 10)
                    head = result
                else:
                    result.next = ListNode(tmp % 10)
                    result = result.next
                carry = tmp // 10
