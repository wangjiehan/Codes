'''
给定一组非负整数 nums，重新排列它们每位数字的顺序使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = [str(token) for token in nums]
        def cmp_(x, y):
            return int(str(x)+str(y)) - int(str(y)+str(x))
        import functools
        arr = sorted(arr, key=functools.cmp_to_key(cmp_), reverse=True)
        return str(int(''.join(arr)))
