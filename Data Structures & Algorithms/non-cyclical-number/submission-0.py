class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        while num != 1:
            temp = 0
            for c in str(num):
                temp += int(c) ** 2
            num = temp
            if temp in seen:
                return False
            seen.add(temp)
        return True