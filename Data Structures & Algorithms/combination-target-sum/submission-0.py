class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        results = []

        copy = []


        def backtrack(start, remaining):

            if remaining == 0:
                results.append(copy[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):
                choice = nums[i]

                copy.append(choice)
                backtrack(i, remaining - choice)
                copy.pop()

        
        backtrack(0, target)
        return results