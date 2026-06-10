class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            last = stones.pop()
            pen = stones[-1]
            if last == pen:
                if len(stones) == 1:
                    return 0
                stones.pop()
            else:
                stones[-1] = last - pen
        return stones[0]