class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use a set to maintain the valid window without repeating characters
        window = set()
        #left side shrinks the window, while right side expands the window.
        l = 0
        res = 0
        for r in range(len(s)):
            #if right side is repeated, shrink left side and remove the element
            while s[r] in window:
                window.remove(s[l])
                l += 1
            #if not repeated, expand the valid window and update the max lenghth
            window.add(s[r])
            res = max(res, r - l + 1)
        return res
