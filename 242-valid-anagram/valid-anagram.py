class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}       #Record character and its frequency
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        for char in t:
            if char not in map:
                return False
            map[char] -= 1

        for m in map:
            if map[m] != 0:
                return False
        return True