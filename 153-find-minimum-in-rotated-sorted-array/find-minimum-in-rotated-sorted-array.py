class Solution:
    def findMin(self, nums: List[int]) -> int:
        # #brute force
        # return min(nums)

        #Binary Search: Find the cliff where the minimum is.
        left, right = 0, len(nums) - 1
        ans = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:             #Cliff is on the right side
                left = mid + 1
            else:
                ans = min(ans, nums[mid])           #Record the num[mid] if it's the minimum number
                right = mid - 1                     #Check if cliff is on the left side

        return ans