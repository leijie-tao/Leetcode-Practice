class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # -------- Two pointers: r to read unique element, and l to write -----------
        n = len(nums)
        l = 0
        for r in range(1, n):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1


        # # -------- Two pointers ---------
        # n = len(nums)
        # l = r = 0
        # while r < n:
        #     if nums[r] == nums[l]:
        #         r += 1
        #     else:
        #         l += 1
        #         nums[l] = nums[r]
        #         r + 1
        # return l + 1
