class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        m = len(set(nums))
        if m == n:
            return False
        else:
            return True