class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # m = len(set(nums))
        # if m == n:
        #     return False
        # else:
        #     return True



        # Refine: Allow return in advance
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False