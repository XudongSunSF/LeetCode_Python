#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head is None or head.next is None or k == 0:
            return head
        count = 0
        node = head
        while node is not None:
            count += 1
            node = node.next
        k %= count
        if k == 0:
            return head
        # move the last k elements to head
        node = head
        for _ in range(count - k - 1):
            node = node.next
        new_tail = node

        new_head = node.next
        while node.next is not None:
            node = node.next
        # now node = tail
        node.next = head
        new_tail.next = None
        return new_head
