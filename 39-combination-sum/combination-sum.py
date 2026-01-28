class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort() 
        def backtrack(remain, start):
            #终止条件
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            #每层逻辑：遍历每个元素递归寻找符合条件的值
            for i in range(start, len(candidates)):
                if remain - candidates[i] < 0:
                    break #优化：先排序，再剪枝（当前位置元素大于remain，则其后都不可能满足条件，直接退出当前循环
                path.append(candidates[i]) #第i位元素入path，递归从i为起点的范围寻找目标值
                backtrack(remain - candidates[i], i) #i为起点（可重复利用同一个元素），继续寻找remain
                path.pop()

        backtrack(target, 0)
        return res

