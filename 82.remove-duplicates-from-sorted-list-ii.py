#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def next_diff_node(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        while head is not None:
            if head.val == val:
                head = head.next
            else:
                break
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        node = head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while node is not None:
            next_node = self.next_diff_node(node.next, node.val)
            if next_node is not node.next:
                prev.next = next_node
                node = prev.next
            else:
                prev = node
                node = node.next
        return dummy.next
