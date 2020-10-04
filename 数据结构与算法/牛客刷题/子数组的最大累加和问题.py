#
# max sum of the subarray
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxsumofSubarray(self , arr ):
        # write code here
        cur = 0
        max_count = float('-inf')
        for i in arr:
            if cur <= 0:
                cur = i
            else:
                cur += i
            if cur > max_count:
                max_count = cur
        return max_count
