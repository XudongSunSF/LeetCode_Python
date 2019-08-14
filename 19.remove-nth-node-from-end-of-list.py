#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        tmp = head
        count = 0
        while tmp is not None:
            count += 1
            tmp = tmp.next

        del_idx = count - n

        if del_idx == 0:
            return head.next
        tmp = head
        for _ in range(del_idx-1):
            tmp = tmp.next
        if tmp.next.next is None:
            tmp.next = None
        else:
            tmp.next = tmp.next.next

        return head
