class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        pre = 0
        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[pre] == 0:
                nums[pre] = nums[i]
                nums[i] = 0
                pre += 1
            if nums[pre] != 0:
                pre += 1

        return nums