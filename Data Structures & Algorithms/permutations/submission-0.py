from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perm = permutations(nums)


        result = []

        for i in list(perm):
            result.append(list(i))

        return result