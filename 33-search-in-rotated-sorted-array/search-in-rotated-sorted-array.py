class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search: has to be used in sorted array
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            #先判断左边是否有序(if left side is sorted: have binary search)
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]: #发现在左侧有序区间内，则直接略过右半边
                    right = mid -1
                else:   #发现不在左侧有序区间内，则略过当前左半边
                    left = mid + 1
            #如果右边有序(else: right side is sorted, and have binary search)
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
        return -1
