class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        x = Counter(nums)

        return any(count >= 2 for count in x.values())