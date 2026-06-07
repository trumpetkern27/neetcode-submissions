class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        i = j = 0
        while j < len(s):
            if s[j] in s[i:j]:
                i += 1
            else:
                l = max(j - i + 1, l)
                j += 1
        return l