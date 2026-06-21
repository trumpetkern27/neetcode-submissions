class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] != s[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            elif not s[i].isalnum():
                i += 1
            else:
                j -= 1
        return True
            