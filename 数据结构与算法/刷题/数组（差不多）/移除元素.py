class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        双指针：
        p1记录所有不等于val的index上限
        cur为游标
        '''
        p1, cur = -1, 0
        while cur < len(nums):
            if nums[cur] != val:
                nums[p1+1] = nums[cur]
                cur += 1
                p1 += 1
            else:
                cur += 1
        return p1 + 1
