import math
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = float("-inf")

        for l in range(len(nums)):
            for r in range(l + 1, len(nums) + 1):
                curr = math.prod(nums[l:r])
                product = max(product, curr)

        return product