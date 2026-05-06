class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target > matrix[mid][-1]:
                top = mid + 1

            elif target < matrix[mid][0]:
                bottom = mid - 1

            else:
                break


        if not (top <= bottom):
            return False
        l = 0
        r = COLS - 1

        current_row = (top + bottom) // 2
        while l <= r:
            mid = (l + r) // 2

            if target > matrix[current_row][mid]:
                l = mid + 1
            elif target < matrix[current_row][mid]:
                r  = mid - 1
            
            else:
                return True
        return False


            
