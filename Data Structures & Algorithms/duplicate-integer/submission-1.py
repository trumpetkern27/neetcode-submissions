class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                return True
        return False