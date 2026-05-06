class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        x = Counter(nums)

        res = sorted(x, key=x.get, reverse=True)

        return (res[:k])