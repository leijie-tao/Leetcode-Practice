class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        res = []
        # 1. Sort
        nums.sort()
        l, r = 0, n - 1
        # 2. Fix first 2 numbers (skip duplicate numbers starting from the second element)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 3. Use two pointers to find the other two numbers (move based on sum value & skip duplicates)
                l, r = j + 1, n - 1
                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                                l += 1
                        while l < r and nums[r] == nums[r + 1]:
                                r -= 1
                    elif four_sum > target:
                        r -= 1
                    else:
                        l += 1
        return res
