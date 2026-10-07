class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        mid_y = bottom // 2
        mid_x = right // 2

        while top <= bottom: 
            if target < matrix[mid_y][0]:
                bottom = mid_y - 1
                mid_y = (top + bottom) // 2
            elif target > matrix[mid_y][-1]:
                top = mid_y + 1
                mid_y = (top + bottom) // 2
            else:
                break

        if top > bottom:
            return False
        
        while left <= right:
            if target < matrix[mid_y][mid_x]:
                right = mid_x - 1
                mid_x = (left + right) // 2
            elif target > matrix[mid_y][mid_x]:
                left = mid_x + 1
                mid_x = (left + right) // 2
            else:
                return True
        
        return False

    # T: O(log(m * n))
    # S: O(1)

