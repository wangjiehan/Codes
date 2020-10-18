# -*- coding:utf-8 -*-

class Finder:
    def findKth(self, a, n, K):
        # write code here
        import  heapq
        return heapq.nlargest(K, a)[K-1]
