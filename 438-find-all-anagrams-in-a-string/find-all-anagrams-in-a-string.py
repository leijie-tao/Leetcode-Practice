class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # ------ Refine: maintain a Counter and reuse it  --> O(n) -------------
        # update window_count everytime, and make sure the size is m
        left = right = 0
        n, m = len(s), len(p)
        if n < m:
            return []

        # maintain a window with m length.
        p_count = Counter(p)
        window_count = Counter()
        res = []

        # Right side to expand the window
        for right in range(n):
            window_count[s[right]] += 1
            # check the length of the window.
            if right - left + 1 > m:
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            # Valid window: same composition & length
            if window_count == p_count:
                res.append(left)
    
        return res



        # # ------ O(n * m): iterate n elements and Counter() iterate m elements. -----------
        # n = len(s)
        # m = len(p)
        # left = right = 0
        # res = []
        # for right in range(n):
        #     if right - left + 1 < m:
        #         continue
        #     if right - left + 1 > m:
        #         left += 1
        #     if right - left + 1 == m:
        #         if Counter(s[left:right + 1]) == Counter(p):
        #             res.append(left)
                
        # return res