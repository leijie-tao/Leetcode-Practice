class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        else:
            target = sum(nums) // 2
        
        # if we can get the sum equal to i
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            # iterate in inverted order to use dp value in last round
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                #if we can get i depends on if we have get i-num or i
            
        return dp[target]