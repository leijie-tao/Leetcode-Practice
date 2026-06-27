class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # record which character is needed
        diff = defaultdict(int)
        for c in t:
            diff[c] -= 1
        need_count = len(diff)
        
        ans_l, ans_r = -1, len(s)
        ge_cnt = 0            #how many characters meet the demand （diff[c] >= 0）
        l = 0

        for r, c in enumerate(s):
            diff[c] += 1      #within the window,  +1
            if diff[c] == 0:  #if the amount is enough, +1
                ge_cnt += 1
            
            #When all the characters are found, try to shrink and find the minimum window
            while ge_cnt == need_count:  
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r #update the answer edges
                
                if diff[s[l]] == 0:     
                    ge_cnt -= 1

                diff[s[l]] -= 1         #move the left side, and mark that one more character is needed.(may not influence ge_cnt)
                l += 1

        if ans_l < 0:
            return ""
        else:
            return s[ans_l:ans_r+1]








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