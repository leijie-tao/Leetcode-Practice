# # --------------------- Brute Force ------------------------
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         tmp = []
#         res = []
#         for p in points:
#             distance = sqrt(p[0]**2 + p[1]**2)
#             # Store as tuple
#             tmp.append((distance, p))
#         # Sort list by first element (distance)
#         tmp.sort(key=lambda x: x[0])
#         for i in range(k):
#             res.append(tmp[i][1])
#         return res

# --------------------- Min Heap ------------------------
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            minHeap.append((dist, x, y))
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            # Unpack and assign value
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
