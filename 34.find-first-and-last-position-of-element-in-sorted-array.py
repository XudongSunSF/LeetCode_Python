#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if nums is None or len(nums) == 0:
            return [-1, -1]

        first, last = -1, -1
        idx = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                idx = mid
                break
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if idx == -1:
            return [first, last]
        else:
            first, last = idx, idx

            while first > 0:
                if nums[first - 1] == target:
                    first = first - 1
                else:
                    break
            while last < len(nums) - 1:
                if nums[last + 1] == target:
                    last += 1
                else:
                    break

            # first_flag, last_flag = False, False
            # while not first_flag or not last_flag:
            #     if first - 1 >= 0 and nums[first - 1] == target:
            #         first = first - 1
            #     else:
            #         first_flag = True

            #     if last + 1 <= len(nums) - 1 and nums[last + 1] == target:
            #         last = last + 1
            #     else:
            #         last_flag = True

        return [first, last]
