import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[\W_]', "", s.replace(" ", "").lower())
        return string == string[::-1]