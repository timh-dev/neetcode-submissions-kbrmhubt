class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # brute force
        #max_profit = 0
        #for i in range(0, len(prices)):
        #    buy = prices[i]
        #    for j in range(i + 1, len(prices)):
        #        sell = prices[j]
        #        max_profit = max(sell - buy, max_profit)
        #return max_profit

        lp = 0
        rp = 1

        max_profit = 0
        while rp < len(prices):
            if prices[lp] < prices[rp]:
                buy = prices[lp]
                sell = prices[rp]
                max_profit = max(sell - buy, max_profit)
            else: 
                lp = rp

            rp += 1

        return max_profit

