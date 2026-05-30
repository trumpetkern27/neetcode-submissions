class Solution:
    def climbStairs(self, n: int) -> int:
        ret = 1
        prev = 0
        for i in range(n):
            temp = ret
            ret += prev
            prev = temp
        return ret