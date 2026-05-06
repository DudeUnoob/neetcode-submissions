from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
       count = Counter(nums)

       print(count)

       sorted_n = sorted(count, key=count.get, reverse=True)

       return sorted_n[:k]