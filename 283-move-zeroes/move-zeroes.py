class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ---------- Two pointers: swap elements------------
        pre = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pre], nums[i] = nums[i], nums[pre]
                pre += 1
        
        

        
        # # ---------- Two pointers: modify the array ------------
        # n = len(nums)
        # l = 0
        # k = 0
        # for r in range(n):
        #     if nums[r] != 0:
        #         nums[l] = nums[r]
        #         l += 1
        #     else:
        #         k += 1

        # for i in range(n-k, n):
        #     nums[i] = 0
        
        
        
        




        