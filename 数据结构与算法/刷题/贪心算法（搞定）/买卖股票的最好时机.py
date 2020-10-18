#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices ):
        # write code here
        '''
        只能买卖一次
        '''
        if len(prices) <= 1:
            return 0
        max_count = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j]-prices[i] > max_count:
                    max_count = prices[j]-prices[i]
        return max(max_count, 0)

class Solution:
    def maxProfit(self, prices):
        '''
        可以买卖多次
        '''
        if len(prices) <= 1:
            return 0
        max_cnt = 0
        i = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                max_cnt += prices[i+1] - prices[i]
        return max(0, max_cnt)
