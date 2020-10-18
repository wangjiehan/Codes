class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        最小元素肯定在非连续部分，找的就是非连续部分
        这是循环前升序排列的数，左边的数小，右边的数大，而且我们要找的是最小值，肯定是偏向左找，所以左右不对称了。
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
