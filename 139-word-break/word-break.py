class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1) #dp[i] 表示字符串s的前i个字符是否可以被拆分成字典中的单词
        dp[0] = True

        for i in range(1, n+1): 
            for j in range(i):
                if dp[j] and s[j:i] in word_set: #check if the word is in the set
                    dp[i] = True
                    break

        return dp[n]
        