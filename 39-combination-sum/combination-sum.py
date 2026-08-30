# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         path = []
#         def backtrack(start, remain):
#             # Find the path that meets the condition ——> add the path
#             if remain == 0:
#                 res.append(path[:])
#                 return
#             elif remain < 0:
#                 return
#             # If it's still searching for candidates, iterate each element and recur each layer
#             else:
#                 for i in range(start, len(candidates)):
#                     path.append(candidates[i])              #Add
#                     backtrack(i, remain - candidates[i])    #Recursion (start from itself(i), and update remain)
#                     path.pop()                              #Remove
#         backtrack(0, target)
#         return res



# -------- Use pruning to refine the code ----------
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort() 
        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return
            # Type 1. Feasibility Pruning：Current path has already violated a constraint, and continuing can only make it worse. So you stop immediately.
            elif remain < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    # Type 2. Ordering-Based (Batch) Pruning: By keeping the candidates sorted, once one choice fails, you can guarantee that every later choice fails too — so you cut off the entire rest of the loop at once.
                    if remain - candidates[i] < 0:
                        break
                    path.append(candidates[i])              
                    backtrack(i, remain - candidates[i]) 
                    path.pop()                          
        backtrack(0, target)
        return res


