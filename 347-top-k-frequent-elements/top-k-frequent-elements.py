class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1: Count & Sort
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        # Use sorted() to sort a list( .keys()) by by a specific key/index.
        count_sorted = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        return count_sorted[:k]
