#Solution2: Dynamic Programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n      #Record the max sum value for the current index
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i]) #Add current nums[i] or restart from this index
            
        return max(dp)