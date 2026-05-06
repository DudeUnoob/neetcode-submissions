class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0

        mDiff = 0


        for r in range(1, len(prices)):
            if prices[left] < prices[r]:
                p = prices[r] - prices[left]
                mDiff = max(mDiff, p)
            
            else:
                left = r

        return mDiff