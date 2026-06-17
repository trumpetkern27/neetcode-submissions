class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        arr = sorted(intervals, key=lambda x: x[0])
        print(arr)
        out = []
        last = arr[0]
        for i in range(1, len(arr)):
            curr = arr[i]
            add = last
            if last[1] >= curr[0]:
                last[1] = max(curr[1], last[1])
                continue
            out.append(add)
            last = curr
        out.append(last)
        return out
            