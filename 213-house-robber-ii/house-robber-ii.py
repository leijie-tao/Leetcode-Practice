class Solution:
    def rob(self, nums: List[int]) -> int:
        #Special nums 
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        #Helper function: calculate the max amount of robbing each house
        def solve_linear(nums):
            #Since we pass sliced nums, we should have special cases
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]

        #Break down the problem: case_a & case_b
        case_a = solve_linear(nums[0:len(nums)-1])
        case_b = solve_linear(nums[1:])
        return max(case_a, case_b)