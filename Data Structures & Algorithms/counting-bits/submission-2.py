import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = []
        i = 0
        while i < n + 1:
            if i == 0:
                ret = [0]
            else:
                ret += (x + 1 for x in ret[:])
            i = len(ret)
        return ret[:n+1]
