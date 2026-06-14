class Solution:
    def findDuplicate(self, nums: List[int]) -> int:      
        # # Method 1: Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        # return -1


        # # Method 2: Sorting
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        # return -1


        #Method 3: Hash Set   (Favorite!!)
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return num
        return -1





