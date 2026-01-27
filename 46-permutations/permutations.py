class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums) #标记每个位置的数字是否已经使用
        def backtrack():
            #终止条件，path满了说明用完所有数字，copy当前path入res
            if len(path) == len(nums):
                res.append(path[:])
                return
            #每层做什么：每层都遍历每一个元素，判断是否用过，把没用过的放入path
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()

                path.pop()  #回溯：不仅要恢复path，还要复原used记录
                used[i] = False
            
        backtrack()
        return res

            
