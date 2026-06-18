import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        def distance(x, y):

            originX = 0
            originY = 0

            return math.sqrt(((0 - x) ** 2) + ((0 - y) ** 2))


        heap = []

        for i in range(len(points)):

            x, y = points[i][0], points[i][1]

            euclidean = distance(x, y)

            heapq.heappush(heap, [ euclidean, points[i] ])

        

        res = []

        for i in range(k):

            smallest = heapq.heappop(heap)

            res.append(smallest[1])
        
        return res