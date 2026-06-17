class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Method 1: sort and iteration. Record current lenghth and update the longest value.
        # nums.sort()
        # res = 0
        # current = 1
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i] == nums[i-1] + 1:
        #         current += 1
        #         res = max(current, res)
        #     else:
        #         current = 1
        # return res


        # # Method 2: Brute force: record & check
        # store = set(nums)           
        # res = 0
        # for num in nums:                #Loop through the list
        #     streak, curr = 0, num       #Start to check from each num
        #     while curr in store:        #keep moving as long as curr + 1 is still in the set
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)      #After checking one num, update the longest value
        # return res


        # Method 3: Refine the code to O(n) ——> add a conditional statement to avoid looping through duplicate sequence
        store = set(nums)
        res = 0
        for num in store:
            #Only start for a new sequence (Skip the elements of previous sequence)
            if num - 1 not in store:
                streak = 1
                #Check the consecutive sequence
                while num + 1 in store:
                    streak += 1
                    num += 1
                #Complete one sequence, and update the longest value
                res = max(res, streak)
        return res