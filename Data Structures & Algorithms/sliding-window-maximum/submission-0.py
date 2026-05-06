class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            maxIndex = nums[i]

            for j in range(i, i + k):
                maxIndex = max(maxIndex, nums[j])

            output.append(maxIndex)

        return output