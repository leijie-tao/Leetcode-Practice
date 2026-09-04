class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  #In case the subarray starts from the first element. (get the valid left side value)
        prefix = 0
        res = 0

        # Iterate each element to be right side. ——> left side is prefix - k (keep the length of range is k)
        for n in nums:
            prefix += n
            res += count[prefix - k]
            count[prefix] += 1
        
        return res

