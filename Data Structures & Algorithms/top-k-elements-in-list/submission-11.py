from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        print(count)

        sorted_n = sorted(count, key=count.get, reverse=True)

        print(sorted_n[:k])

        return sorted_n[:k]