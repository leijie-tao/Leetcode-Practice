class Solution:
    # Similar with 1248.Count Number of Nice Subarrays.
    # (prefix[j] - prefix[i]) % k == 0 区间和能被k整除 ————> prefix[i] and prefix[j] have the same remainder ——> count the number of same remainder
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count =defaultdict(int)
        count[0] = 1
        prefix = 0
        res = 0

        for n in nums:
            prefix += n
            remainder = prefix % k
            # Update res first, since we need the number of the remainder before current element
            res += count[remainder]
            count[remainder] += 1 
        
        return res