class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # k may be larger than n
        k = k % n 

        # Use slice ([:] on the right) of list to revise nums in place ([:] on the left)
        back = nums[n-k:]     # slice ——> copy of some parts (new list)
        front = nums[:n-k]       
        nums[:] = back + front  # [:] ——> revise original list (no new list)