class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # ------------ O(n) ---------
        left = 0
        window_sum = 0     
        res = float('inf')
        for right in range(len(nums)):
            window_sum += nums[right]
            # meet requirement first, and then try to shrink window
            while window_sum >= target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]    # update sum first in case that left changes
                left += 1

        if res == float('inf'):
            return 0
        else:
            return res

            