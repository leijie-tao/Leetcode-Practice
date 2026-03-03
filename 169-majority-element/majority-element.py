class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        return max(d, key = d.get) #max()遍历字典中的key，比较的依据是key对应的值key = d.get