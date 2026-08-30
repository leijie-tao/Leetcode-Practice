class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort() 
        def backtrack(start, remain):
            # Find the path that meets the condition ——> add the path
            if remain == 0:
                res.append(path[:])
                return
            elif remain < 0:
                return
            # If it's still searching for candidates, iterate each element and recur each layer
            else:
                for i in range(start, len(candidates)):
                    path.append(candidates[i])              #Add
                    backtrack(i, remain - candidates[i])    #Recursion (start from itself(i), and update remain)
                    path.pop()                              #Remove
        backtrack(0, target)
        return res



