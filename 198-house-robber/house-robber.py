class Solution:
    def rob(self, nums: List[int]) -> int:
        #Special cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #Base cases
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i]) #State Transition Equation
        
        return dp[len(nums)- 1]
        