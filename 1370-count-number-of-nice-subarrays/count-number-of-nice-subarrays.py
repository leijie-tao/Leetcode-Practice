class Solution:
    # Only care about odd and even, instead of values. ——> use 1 and 0 to replace values ——> find subarrays, sum of which is k
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Use count to record how many arrays have the same prefix
        count = defaultdict(int)
        count[0] = 1 
        # Use prefix (right side) to record the sum from start to current element ——> prefix - k (left side)
        prefix = 0  
        res = 0 

        #Iterate to update prefix (Have each element to be right side) ——> Find valid left side
        for n in nums:
            if n % 2 == 1:
                prefix += 1
            # Record new prefix and add valid count into res
            count[prefix] += 1
            res += count[prefix - k]
            
        return res