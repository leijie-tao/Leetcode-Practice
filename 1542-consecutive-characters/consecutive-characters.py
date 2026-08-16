class Solution:
    # -------------- Brute Force -----------------
    # def maxPower(self, s: str) -> int:
    #     n = len(s)
    #     max_count = 1
    #     for i in range(n):
    #         count = 1
    #         for j in range(i+1, n):
    #             if s[j] == s[j - 1] and s[i] == s[j]:
    #                 count += 1
    #                 max_count = max(max_count, count)
    #             else:
    #                 break
            
    #     return max_count

    
    def maxPower(self, s: str) -> int:
        max_count = 1
        count = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1

        return max_count
