#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


class Solution:
    def reverse(self, x: int) -> int:

        if x == 0:
            return x
        isPositive = True if x > 0 else False

        if not isPositive:
            x *= -1
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            if result > 2 ** 31 - 1:
                result = 0
                break
            x = x // 10

        if not isPositive:
            result *= -1

        return result
