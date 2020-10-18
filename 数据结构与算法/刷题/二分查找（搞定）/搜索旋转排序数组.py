class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:  # 左半段有序
                if target <= nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[left]: # 无法判断
                left += 1
            else:                       # 右半段有序
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class Solution:
    '''
    判断给定的目标值是否存在于数组中
    '''
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:  # 左半段有序
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[left]:   # 无法判断
                left += 1
            else:                       # 右半段有序
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
