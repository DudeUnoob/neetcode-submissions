class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        current_max = float('-inf')

        for i in range(len(nums) - k + 1):
            
            window = nums[i: i + k]
            current_max = max(window)
            res.append(current_max)

        return res