class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        my_dict = { x: nums.count(x) for x in set(nums) }

        return sorted(my_dict, key=my_dict.get, reverse=True)[0]

        