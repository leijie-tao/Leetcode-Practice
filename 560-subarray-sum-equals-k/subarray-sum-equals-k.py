class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Use count to record how many times does the prefix value occur.
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


# Subarray <——> (i, j] <——> Subarray Sum = prefix[j] - prefix[i]  <——> 遍历每个元素作为右端点，查看对应的左端点prefix-k出现了几次（默认0次）  <——>  添加有效区间的个数到res，即为满足条件的subarray
