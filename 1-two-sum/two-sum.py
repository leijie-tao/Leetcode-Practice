class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        #Hash Map
        visited = {}                #Store in hash map, and support searching index by number value
        for i in range(len(nums)):
            need = target - nums[i]     
            if need not in visited:     #If don't find needed number, store it first. {number: index}
                visited[nums[i]] = i    
            else:
                return [i, visited[need]]   #If find the needed number, return the index
