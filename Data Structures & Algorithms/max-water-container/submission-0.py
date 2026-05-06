class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        maxHeight = 0

        while left < right:
            currentHeight = min(heights[left], heights[right]) * (right - left)
            maxHeight = max(maxHeight, currentHeight)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxHeight