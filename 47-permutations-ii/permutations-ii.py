class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums) 
        nums.sort() #与组合去重同理，先排序
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue #增加重复时的跳过：i>0第二位起，当元素等于上个元素，且上个元素在used中是false状态
                             #used[i-1]==false说明i-1已经递归完成溯洄了，此时相同元素为首的情况已经寻找完毕

                used[i] = True
                path.append(nums[i])
                backtrack()

                path.pop()  
                used[i] = False
            
        backtrack()
        return res