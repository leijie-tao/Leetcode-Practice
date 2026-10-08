class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""
        # for loop to check each index
        for i in range(len(strs[0])):
            # check if each element has the same prefix at index i
            for s in strs:
                # Stop condition: 1. out of range     2. find an element that doesn't have the prefix at index i
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += s[i]
        return res