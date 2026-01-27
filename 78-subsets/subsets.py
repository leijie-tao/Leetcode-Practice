class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            res.append(path)
            if start == len(nums): #终止条件
                return
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]]) #对每个第i位的数，向下递归层层寻找i+1之后数的子集
                # path + nums[i]即为初始path+每一层的nums[i]，没有修改path本身因此回溯时不需要pop
                
        backtrack(0, [])
        return res
