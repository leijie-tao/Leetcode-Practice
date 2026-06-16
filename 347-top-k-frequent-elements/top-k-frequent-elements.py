class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Method 1: Count & Sort
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        # # Use sorted() to sort a list( .keys()) by by a specific key/index.
        # count_sorted = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        # return count_sorted[:k]



        # Method 2: Heap (easy to catch the max/min)
        count = Counter(nums)
        # Create min heap to store top k (max frequency) ——> avoid storing all elements
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:       # Make sure only store k elements
                heapq.heappop(heap)
        
        # Loop through the heap, and add each num into result
        res = []
        for freq, num in heap:
            res.append(num)
        return res
