class Solution:
    def maxProfit(self,prices:List[int])->int:
        minPriceSoFar = prices[0]
        maxProfitSoFar = 0
        n = len(prices)
        for i in range(1,n):
            if minPriceSoFar > prices[i]:
                minPriceSoFar = prices[i]
            if maxProfitSoFar < (prices[i]-minPriceSoFar):
                maxProfitSoFar = prices[i]-minPriceSoFar
        return maxProfitSoFar
