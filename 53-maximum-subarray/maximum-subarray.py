
class Solution:
    #Solution1: Kadane Algrithm       DP & greedy 
    # -------TC O(n)    SC O(1)------------
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            # if current sum is negative, reset the start of subarray
            if cur_sum < 0:
                cur_sum = 0
            # calculate current sum and update max
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum




    #Solution2: Dynamic Programming
    # def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n      #Record the max sum value for the current index
        # dp[0] = nums[0]

        # for i in range(1, n):
        #     dp[i] = max(nums[i], dp[i-1] + nums[i]) #use max to choose adding current nums[i] or restarting from this index
            
        # return max(dp)