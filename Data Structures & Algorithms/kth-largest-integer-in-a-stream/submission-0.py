class KthLargest:
    arr: List[int]
    k: int
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.arr = nums
        self.k = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[-self.k]
