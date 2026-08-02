# ------------------- Brute Force --------------------------
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort(reverse = True)
#         return nums[k - 1]


# ------------------- Min Heap --------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
