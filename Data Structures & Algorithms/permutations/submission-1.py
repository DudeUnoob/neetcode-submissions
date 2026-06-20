

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []


        def backtrack(index, path):
            
            if index == len(nums):
                res.append(path[:])
                return

            for i in nums:
                if i in path:
                    continue
                
                path.append(i)
                backtrack(index + 1, path)
                path.pop()


        backtrack(0, [])

        return res