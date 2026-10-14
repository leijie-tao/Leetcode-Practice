class Solution:
    # --------- O(n) ------------
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        left = right = 0
        k = 0
        while right < n:
            if nums[right] != val:
                k += 1
                nums[left] = nums[right]
                right += 1
                left += 1
            else:
                right += 1
        return k

