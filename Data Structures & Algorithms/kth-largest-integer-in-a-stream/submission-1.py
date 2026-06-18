class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.heap = nums
        self.k = k


        self.maxHeap = []

        for i in range(len(self.heap)):
            heapq.heappush(self.maxHeap, -self.heap[i])

        print(self.maxHeap)



    def add(self, val: int) -> int:
        
        heapq.heappush(self.maxHeap, -val)

        largest = None
        popped = []

        for i in range(self.k):
            largest = -heapq.heappop(self.maxHeap)
            popped.append(-largest)

        for num in popped:
            heapq.heappush(self.maxHeap, num)

        return largest