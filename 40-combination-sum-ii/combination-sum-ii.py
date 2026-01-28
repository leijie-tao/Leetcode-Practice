class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = []
        candidates.sort()
        def backtrack(remain, start):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                if remain - candidates[i] < 0:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue #跳过重复的起始值
                path.append(candidates[i])
                backtrack(remain - candidates[i], i + 1) #递归i+1开始，不能引用自己
                path.pop()
        
        backtrack(target, 0)
        return res

