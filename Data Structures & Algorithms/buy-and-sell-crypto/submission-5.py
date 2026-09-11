class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[i] < prices[j]:                   #my code (BRUTE FORCE) O(n^2) 
        #             profit = prices[j] - prices[i]
        #             max_profit = max(profit, max_profit) 

        # return max_profit

        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)

            else:
                l = r
            r+=1
        
        return max_profit

