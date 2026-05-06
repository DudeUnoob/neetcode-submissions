class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        top, bott = 0, rows - 1                  

        mid = 0

        while top <= bott:
            mid = (top + bott) // 2
            if matrix[mid][-1] < target:         
                top = mid + 1
            elif matrix[mid][0] > target:        
                bott = mid - 1
            else:                                
                break


        print(mid)


        current_array = matrix[mid]

        left, right = 0, len(current_array) - 1

        while left <= right:
            midd = (right + left) // 2

            if current_array[midd] > target:
                right = midd - 1
            
            elif current_array[midd] < target:
                left = midd + 1
            else:
                return True
        
        return False

