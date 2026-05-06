class Solution:
    def findMin(self, nums: List[int]) -> int:

        mini = min(nums)

        nums.sort()
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == mini:
                return nums[mid]

            elif nums[mid] > mini:
                right = mid - 1

            elif nums[mid] < mini:
                left = mid + 1

            
        return nums[mid]