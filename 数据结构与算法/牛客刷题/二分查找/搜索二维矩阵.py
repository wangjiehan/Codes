class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        r, c = 0, len(matrix[0]) - 1
        while r >=0 and r <= len(matrix) - 1 and c >= 0 and c <= len(matrix[0]) - 1:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
