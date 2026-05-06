class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [0] * len(nums)

        for i in range(len(nums)):
            current = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                
                current *= nums[j]

            result[i] = current

        return (result)


        