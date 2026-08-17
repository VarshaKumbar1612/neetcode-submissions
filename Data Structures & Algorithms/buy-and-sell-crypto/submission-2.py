class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_index = prices.index(min(prices))
        # max_price = 0
        # for i in range(min_index, len(prices)):
        #     if prices[i]>max_price:
        #         max_price = prices[i]
        # profit = max_price - min(prices)
        # if profit > 0:
        #     return profit
        # else:
        #     return 0
        
        if len(prices) <= 1:
            return 0
        
        res = []
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                else:
                    profit = 0
                res.append(profit)
        return max(res) 


