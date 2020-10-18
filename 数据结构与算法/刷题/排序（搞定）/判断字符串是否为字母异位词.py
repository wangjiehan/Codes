class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def _str_to_list(s):
            return [i for i in s]
        return sorted(_str_to_list(s)) == sorted(_str_to_list(t))
