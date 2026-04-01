class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        res = max_p = min_p = nums[0]

        for i in range(1, n):
            f, g = max_p, min_p
            max_p = max(nums[i], f * nums[i], g * nums[i]) #Calculate maximum product for current
            min_p = min(nums[i], f * nums[i], g * nums[i]) #Get potential negative numbers
            res = max(res, max_p) #Record the maximum profuct for the whole process

        return res
