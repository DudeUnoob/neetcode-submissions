import heapq

class MedianFinder:

    def __init__(self):

        self.heap = []
        

    def addNum(self, num: int) -> None:

        self.heap.append(num)

        self.heap.sort()


    def findMedian(self) -> float:
        
        l = 0
        r = len(self.heap) - 1

        if len(self.heap) % 2 == 1:

            return self.heap[(l + r) // 2]

        else:

            while l < r:

                l += 1
                r -= 1

            return ((self.heap[l] + self.heap[r]) / 2)
        