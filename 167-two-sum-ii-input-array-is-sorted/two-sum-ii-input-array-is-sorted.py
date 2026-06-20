class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Hash map: record the index and value, and check
        visited = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in visited:
                return [visited[diff], i + 1]
            else:
                visited[n] = i + 1
        
            
        
        
