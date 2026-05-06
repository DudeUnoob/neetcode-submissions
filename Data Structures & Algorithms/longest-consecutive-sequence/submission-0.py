class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for i in seen:
            if i - 1 not in seen:  # Start of a sequence
                length = 1
                current = i + 1
                while current in seen:
                    length += 1
                    current += 1
                res = max(res, length)

        return res
