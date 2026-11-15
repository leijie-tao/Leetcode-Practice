# maximum product is different from sum since we can't discard negative number directly. We need to record maximum and minimum at the same time.

class Solution:
    #  # DP: use 2 dp tables in case negative number flips to a positive one
    # def maxProduct(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     max_dp = [0] * n
    #     min_dp = [0] * n
    #     max_dp[0] = min_dp[0] = nums[0]
    #     for i in range(1, n):
    #         num = nums[i]
    #         max_dp[i] = max(num, max_dp[i - 1] * num, min_dp[i - 1] * num)
    #         min_dp[i] = min(num, max_dp[i - 1] * num, min_dp[i - 1] * num)

    #     return max(max_dp)

    

    # Kadane's Algorithm: use 2 cur variables to record
    def maxProduct(self, nums: List[int]) -> int:
        maximum = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            # if meet negative numvers, swap the 2 variables
            if nums[i] < 0 :
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])
            maximum = max(maximum, cur_max)
        
        return maximum
