class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 9999
        maxProfit = 0
        for a in range(len(prices)):
            if(prices[a] < minPrice):
                minPrice = prices[a]
            elif(prices[a] - minPrice > maxProfit):
                maxProfit = prices[a] - minPrice
        return maxProfit
