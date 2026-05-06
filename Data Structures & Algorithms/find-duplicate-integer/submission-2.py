class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        my_dict = { x: nums.count(x) for x in set(nums) }

        for i in my_dict:
            if my_dict[i] >= 2:
                return i

        