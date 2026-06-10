class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        l = 0

        r = len(numbers) - 1

        nums = numbers
        while l < r:

            if target < nums[l] + nums[r]:
                r -= 1

            elif target > nums[l] + nums[r]:
                l += 1

            else:
                return [l + 1, r + 1]

        
