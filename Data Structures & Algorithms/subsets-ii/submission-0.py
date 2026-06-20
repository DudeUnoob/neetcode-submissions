class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(index, path):

            if index == len(nums):
                res.append(path[:])
                return

            
            if index >= len(nums):
                return

            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)



        res.sort()
        backtrack(0, [])
        
        res = [sorted(tuple(i)) for i in res]
        seen = set()
        
        result = []

        for i in res:

            i_tuple = tuple(i)

            if i_tuple not in seen:
                seen.add(i_tuple)
                result.append(i)

        return result

        

