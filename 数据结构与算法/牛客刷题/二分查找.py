#
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
#
class Solution:
    def upper_bound_(self , n , v , a ):
        # write code here
        left, right = 0, n - 1
        while left <= right:
            mid = (left+right) // 2
            if a[mid] < v:
                left = mid + 1
            elif a[mid] > v:
                right = mid - 1
            else:
                if mid == 0 or a[mid-1] != v:
                    return mid + 1
                else:
                    right = mid - 1
        return left + 1