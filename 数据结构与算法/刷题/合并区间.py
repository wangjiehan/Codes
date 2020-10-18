# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

#
# 
# @param intervals Interval类一维数组 
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals ):
        # write code here
        intervals_ = sorted(intervals, key=lambda x:x.start)
        res = []
        for i in intervals_:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(i.end, res[-1].end)
        return res
