class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])


        top = 0
        bottom = ROWS - 1

        mid = 0

        while top <= bottom:

            mid = (top + bottom) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            
            elif matrix[mid][0] > target:
                bottom = mid - 1
            
            else:
                break

        

        print(matrix[mid], target)

        nums = matrix[mid]

        l = 0
        r = len(nums) - 1

        while l <= r:

            middle = (l + r) // 2

            if target > nums[middle]:
                l = middle + 1

            elif target < nums[middle]:
                r = middle - 1

            else:
                return True

        return False

        