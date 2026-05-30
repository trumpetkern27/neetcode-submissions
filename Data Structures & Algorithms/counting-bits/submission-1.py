import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        max_int = 2**31 - 1
        i = 0
        while i < n + 1:
            if i == 0:
                ret = [0]
            else:
                ret += (x + 1 for x in ret[:])
            i = len(ret)
        return ret[:n+1]
