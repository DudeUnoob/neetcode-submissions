import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = []

        for i in range(len(nums)):

            heapq.heappush(maxHeap, -nums[i])

        
        largest = None

        for i in range(k):

            largest = -heapq.heappop(maxHeap)

        return largest