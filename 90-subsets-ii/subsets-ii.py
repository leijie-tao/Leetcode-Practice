class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort() #排序让重复的数放在一起
        def backtrack(start): 
            res.append(path[:])
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue    #i>start在同层，如果当前数等于前一个数，则说明已经处理过，可以跳过
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res