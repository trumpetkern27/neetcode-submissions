class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            r += (n % 2) << (31 - i)
            n = n >> 1
        return r
        