#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


class Solution:
    def rob(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        if length == 2:
            return max(nums)

        dp = [0]*length  # assign dp array
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        print(dp)

        return max(dp)
