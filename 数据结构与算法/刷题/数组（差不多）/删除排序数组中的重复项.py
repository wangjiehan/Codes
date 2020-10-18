'''
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		'''
		双指针法
		'''
		p1, p2 = 0, 0
		while p2 < len(nums):
			if nums[p2] != nums[p1]:
				nums[p1+1], nums[p2] = nums[p2], nums[p1+1]
				p1 += 1
				p2 += 1
			else:
				p2 += 1
		return p1 + 1

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		nums[:] = sorted(list(set(nums)))
		return len(nums)
