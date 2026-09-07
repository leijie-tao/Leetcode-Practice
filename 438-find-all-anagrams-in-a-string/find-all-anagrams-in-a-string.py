class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = 0
        n, m = len(s), len(p)
        if n < m:
            return []

        # Compare character composition
        p_count = Counter(p)
        window_count = Counter()
        res = []

        # Right side to expand the window
        for right in range(n):
            window_count[s[right]] += 1
            # Keep the length of the window. When exceed, shrink the window with left side.
            if right - left + 1 > m:
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1
            # Valid window: same composition & length
            if window_count == p_count:
                res.append(left)

        
        return res
