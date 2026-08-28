class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start):
            # record the copy of path without conditions
            res.append(path[:])
            # Key point: use start to control where is the start of next layer in recursion
            # Record all subsets starts from nums[i]
            for i in range(start, len(nums)):
                path.append(nums[i])  #Add path
                backtrack(i + 1)    #Recursion from i+1
                path.pop()          #Withdraw the last node of current layer
                # Go back to root, and continue for loop
                
        backtrack(0)
        return res

