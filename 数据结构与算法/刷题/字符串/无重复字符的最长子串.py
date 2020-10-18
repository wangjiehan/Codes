'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        max_len = 0
        tmp = ''
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp += s[i]
            else:
                tmp = tmp[tmp.index(s[i])+1:]
                tmp += s[i]
            if len(tmp) > max_len:
                max_len = len(tmp)
        return max_len
