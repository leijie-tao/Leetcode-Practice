class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n):
            #max_reach failed: check if every position can be reached
            if i > max_reach:
                return False
            #Update the current max_reach
            max_reach = max(max_reach, i + nums[i])

            #max_reach success: if max_reach is larger than the last element, return True directly
            if max_reach >= n - 1:
                    return True

        #Edge case:nums = []       
        return False
        