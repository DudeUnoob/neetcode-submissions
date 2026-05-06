class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1

        right = max(piles)

        res = 0

        while left <= right:
            totalHours = 0
            
            k = (left + right) // 2
            for p in piles:
                totalHours += math.ceil(p / k)

            if totalHours <= h:

                right = k - 1
                res = k

            
            else:
                left = k + 1

        return res