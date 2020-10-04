#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices ):
        # write code here
        if len(prices) <= 1:
            return 0
        max_count = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > max_count:
                    max_count = prices[j]-prices[i]
        return max_count if max_count >= 0 else 0
