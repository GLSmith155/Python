  # My single for-loop solution for https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
  # Faster than 97% of other solutions.
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowPoint = prices[0]
        greatestRange = 0
        
        for count, value in enumerate(prices):
            
            if (value > lowPoint):
                newRange = value - lowPoint
                
                if (greatestRange < newRange):
                    greatestRange = newRange
                    
            if (value < lowPoint):
                lowPoint = value
            
        if (greatestRange < 0):
            greatestRange = 0
            
        return greatestRange
