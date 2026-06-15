from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)     
        #Counter() will loop through the string, count for each element, and return{"a": 3, "g": 1,...}



        ## Hash map
        # if len(s) != len(t):
        #     return False
        
        # map = {}       #Record character and its frequency
        # for char in s:
        #     if char not in map:
        #         map[char] = 1
        #     else:
        #         map[char] += 1
        # for char in t:
        #     if char not in map:
        #         return False
        #     map[char] -= 1

        # for m in map:
        #     if map[m] != 0:
        #         return False
        # return True