# # -------------------- Brute Force ------------------------
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         # Count the number of each element
#         count = defaultdict(int)
#         for t in tasks:
#             count[t] += 1
        
#         # Record current available tasks and start from the largest quantity
#         res = 0
#         while count:
#             executed = 0
#             available = []
#             for task, cnt in count.items():
#                 if cnt > 0:
#                     available.append(task)
#             available.sort(key=lambda x: count[x], reverse=True)

#             # Execute all the tasks, delete the completed task, and update the quantity
#             for i in range(min(n + 1, len(available))):
#                     task = available[i]
#                     count[task] -= 1
#                     if count[task] == 0:
#                         del count[task]
#                     executed += 1
#                     res += 1

#             # If there are still other tasks, add intervals
#             if count:
#                     res += (n + 1 - executed)
        
#         return res



# -------------------- Max Heap ------------------------
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for cnt in count.values():
            maxHeap.append(-cnt)
        heapq.heapify(maxHeap)

        time = 0
        cooldown = deque()  # pairs of [-cnt, idleTime]
        # While there are available tasks or in cooldown 
        while maxHeap or cooldown:
            time += 1
            # Available tasks: Update time with the cooldown ending time
            if not maxHeap:
                time = cooldown[0][1]
            # Cooldown tasks: pop the task with largest quantity. If there are still tasks, add it to cooldown queue with updated ending time
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    cooldown.append([cnt, time + n])
            # Check if the cooldown tasks are ready to go to maxHeap to be executed.
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])
        return time
        