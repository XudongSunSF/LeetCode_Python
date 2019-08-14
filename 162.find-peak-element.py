#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if nums is None and len(nums) == 0:
            return
        n = len(nums)
        if n == 1:
            return 0
        left, right = 0, n-1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        return left if nums[left] > nums[right] else right
