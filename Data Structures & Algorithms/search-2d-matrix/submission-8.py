class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        bottom = len(matrix) - 1
        top = 0

        middle = 0

        while top <= bottom:

            middle = (top + bottom) // 2

            if matrix[middle][-1] < target:
                top = middle + 1
            
            elif matrix[middle][0] > target:
                bottom = middle - 1
            
            else:
                row = matrix[middle]

                left = 0
                right = len(row) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if target == row[mid]:
                        return True
                    
                    elif target > row[mid]:
                        left = mid + 1
                    
                    else:
                        right = mid - 1
                return False
        return False
                    


