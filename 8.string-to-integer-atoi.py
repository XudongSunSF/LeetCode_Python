#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


class Solution:
    def myAtoi(self, str: str) -> int:

        # check if str is a string
        if not str:
            return 0
        # remove white space
        str = str.strip()
        # check if str is an empty string after removing white spaces
        if not str:
            return 0
        number, sign = 0, 1

        # check if the first char is '-'
        if str[0] == '-':
            # check if the str only contains '-'
            if len(str) == 1:
                return 0
            str = str[1:]
            sign = -1
        elif str[0] == '+':
            if len(str) == 1:
                return 0
            str = str[1:]
        for c in str:
            if c >= '0' and c <= '9':
                number = 10*number + ord(c) - ord('0')
            else:
                break
        number = sign * number
        number = number if number <= 2147483647 else 2147483647
        number = number if number >= -2147483648 else -2147483648
        return number
