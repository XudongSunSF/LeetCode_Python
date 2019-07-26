#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a_map = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in a_map:
                a_map[num] = i
            else:
                return [a_map[n], i]
