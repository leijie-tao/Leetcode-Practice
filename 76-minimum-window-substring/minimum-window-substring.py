class Solution:
    # ------ O(n + m): right&left pointers-> O(2n), counter(t)-> O(m) ----------
    def minWindow(self, s: str, t: str) -> str:
        # substring includes t  ---> count characters
        target = Counter(t)
        window = Counter()
        left = 0
        matched = 0  #use match to avoid discussing extra characters in window
        need_match = len(target)
        min_length = float('inf')
   
        for right in range(len(s)):
            # add characters into window, and record matched
            window[s[right]] += 1
            if s[right] in target and window[s[right]] == target[s[right]]:
                matched += 1
            
            # when t is contained by window, start to shrink window: check length, record start, remove element and update mathched
            while matched == need_match:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_start = left
                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    matched -= 1
                left += 1
        
        if min_length == float('inf'):
            return ""
        else:
            return s[min_start:min_start + min_length]










        # count = Counter(t)

        # l = 0
        # matched = 0
        # min_len = float('inf')
        # res = ""
        # window = Counter()

        # for r in range(len(s)):
        #     window[s[r]] += 1
        #     if window[s[r]] == count[s[r]]:
        #         matched += 1
        
        #     while matched == len(t):
        #         if r - l + 1 < min_len:
        #             min_len = r - l + 1
        #             res = s[l:r+1]
                
        #         window[s[l]] -= 1
        #         if window[s[l]] < count[s[l]]:
        #             matched -= 1
        #         l += 1

        # return res