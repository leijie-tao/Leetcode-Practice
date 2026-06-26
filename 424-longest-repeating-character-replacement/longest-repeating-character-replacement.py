class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # avoid repeating (set) ——> allow limited repeating (map to record)
        # use map & while non-repetive < k
        count = defaultdict(int)
        l = 0
        max_freq = 0
        res = 0
        for r in range(len(s)):
            # record the frequency and find the irreplaceable element with max frequency.
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            # while window is invalid, shrink
            while r - l + 1 - max_freq > k:
                count[s[l]] -= 1
                l += 1
            #otherwise, record current longest character
            res = max(res, r - l + 1)

        return res


