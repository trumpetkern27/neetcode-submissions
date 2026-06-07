class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}
        for c in s1:
            chars[c] = chars.get(c, 0) + 1
        for i in range(len(s2)):
            temp = {}
            for j in range(len(s1)):
                if i + j >= len(s2):
                    break
                temp[s2[i + j]] = temp.get(s2[i + j], 0) + 1
            if temp == chars:
                return True
        return False