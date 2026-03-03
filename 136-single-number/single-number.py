class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for n in nums:
            if d[n] == 1:
                return n