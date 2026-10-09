class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            else:
                window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])
        return False