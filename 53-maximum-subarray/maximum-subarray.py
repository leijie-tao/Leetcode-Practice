#Solution1: Greedy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            # if cur_sum + nums[i] is less than nums[i], which means cur_sum is negative and we can start from nums[i] directly.
            cur_sum = max(nums[i], cur_sum + nums[i])
            # record the maximum value
            max_sum = max(max_sum, cur_sum)
            
        return max_sum