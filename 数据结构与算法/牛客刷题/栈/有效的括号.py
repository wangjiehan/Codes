class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ('(', '[', '{'):
                stack.append(i)
            if i in (')', ']', '}'):
                if not stack:
                    return False
                else:
                    if (i==')' and stack[-1]=='(') or (i==']' and stack[-1]=='[') or (i=='}' and stack[-1]=='{'):
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False
