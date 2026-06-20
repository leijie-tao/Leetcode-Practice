class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # similar with Two Sum(array sorted) ——> two pointers
        res = []
        
        #Loop through the sorted list, and search for target numbers on the right side of each n (avoid duplicates)
        for i, n in enumerate(nums):
            if n > 0:   #If n > 0, we don't need to look at elements on the rihgt
                break
            if i > 0 and n == nums[i - 1]:  #If n has appeared, continue to the next element
                continue
            
            #Same as Two Sum(array sorted)
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = n + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([n, nums[left], nums[right]])
                    left += 1       #Keep searching
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:    #Avoid duplicate and invalid range
                        left += 1
        
        return res

