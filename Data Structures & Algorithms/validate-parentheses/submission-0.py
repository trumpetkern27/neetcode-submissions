class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '[', '{'}
        closing = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in closing:
                stack.append(closing[c])
            else:
                if stack == [] or stack.pop() != c:
                    return False
        return stack == []