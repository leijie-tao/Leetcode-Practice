class Solution:
    # -------------- Optimal: Boyer-Moore Majority Voting Algorithm --------------
    # ------------- TC: O(n)    SC: O(1) -----------------
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate



    # # -------------- TC: O(n + mlogm) -------------------
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = Counter(nums)     #TC: O(n)
    #     d = sorted(count, key = lambda k: count[k], reverse = True)     #TC: O(mlogm)
    #     return d[0]