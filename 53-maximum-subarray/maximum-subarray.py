
class Solution:
    #Solution1: Kadane Algrithm (refine dp by saving more space)
    # ------- O(n) ------------
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, len(nums)):
            # maximum subarray for i can be itself or (previous + nums[i])
            cur_sum = max(nums[i], cur_sum + nums[i])
            # update maximum subarray for the whole array
            max_sum = max(max_sum, cur_sum)
        return max_sum




    #Solution2: Dynamic Programming
    # def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n      #Record the max sum value for the current index
        # dp[0] = nums[0]

        # for i in range(1, n):
        #     dp[i] = max(nums[i], dp[i-1] + nums[i]) #Add current nums[i] or restart from this index
            
        # return max(dp)