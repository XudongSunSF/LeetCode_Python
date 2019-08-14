#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or len(matrix) == 0:
            return False
        nrows = len(matrix)
        ncols = len(matrix[0])

        # treat 2d matrix as a 1d array
        left, right = 0, nrows * ncols - 1
        while left <= right:
            mid = (left + right) // 2
            row_idx = mid // ncols
            col_idx = mid % ncols

            if matrix[row_idx][col_idx] < target:
                left = mid + 1
            elif matrix[row_idx][col_idx] > target:
                right = mid - 1
            else:
                return True
        return False
