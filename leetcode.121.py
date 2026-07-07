class Solution(object):
    def maxProfit(self, prices):
        min1 = prices[0]
        r = 0

        for i in range(1, len(prices)):
            if prices[i] < min1:
                min1= prices[i]
            else:
                r= max(r, prices[i] - min1)

        return r
        
