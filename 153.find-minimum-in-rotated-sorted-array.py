#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return - 1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left] if nums[left] < nums[right] else nums[right]
