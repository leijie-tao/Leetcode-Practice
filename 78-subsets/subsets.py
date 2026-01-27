class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start):
            res.append(path[:])
            if start == len(nums): #终止条件
                return
            for i in range(start, len(nums)):
                path.append(nums[i]) #path内暂存第i位元素
                backtrack(i + 1) #递归层层向下直到start==len(nums)折返，寻找以i为起点的所有子集
                path.pop()#每次弹出最后一位数，回到上一层
        backtrack(0)
        return res
