import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        copy = []
        
        for i in range(len(stones)):

            heapq.heappush(copy, -stones[i])
        
        
        while len(copy) > 1:
            
            x, y = -heapq.heappop(copy), -heapq.heappop(copy)

            if x == y:
                continue

            elif x > y:

                heapq.heappush(copy, - (x - y))


        if copy:
            return -copy[0]

        return 0




