class Solution:
    # --------- O(n) Two pointers: read & write ------------
    def removeElement(self, nums: list[int], val: int) -> int:
        # n = len(nums)
        # left = right = 0
        # k = 0
        # while right < n:
        #     if nums[right] != val:
        #         k += 1
        #         nums[left] = nums[right]
        #         right += 1
        #         left += 1
        #     else:
        #         right += 1
        # return k

        n = len(nums)
        left = 0        # write pointer(slow)
        k = 0
        for right in range(n):      # read pointer(fast)
            if nums[right] == val:
                continue
            else:
                k += 1
                nums[left] = nums[right]
                left += 1
        return k

