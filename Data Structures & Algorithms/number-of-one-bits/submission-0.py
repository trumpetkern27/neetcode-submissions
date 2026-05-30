class Solution:
    def hammingWeight(self, n: int) -> int:
        b = 0
        while n != 0:
            if n % 2 != 0:
                b += 1
                n -= 1
            n /= 2
        return b