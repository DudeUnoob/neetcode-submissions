class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cost = [0] * len(nums)

        def dfs(i):

            if i >= len(nums):
                return 0

            
            if cost[i]:
                return cost[i]

            
            cost[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

            return cost[i]


        return max(dfs(0), dfs(1))