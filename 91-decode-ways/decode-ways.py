class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # dp[i] 表示前 i 个字符的解码方法数
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[1] = 1

        #dp[i] = (由 1 位数解码带来的方案) + (由 2 位数解码带来的方案)
        for i in range(2, n+1):
            #当前一位数s[i-1]
            one_digit = int(s[i-1])
            if one_digit != 0:
                dp[i] += dp[i-1]
            #最后两个数字s[i-2:i]
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]

        return dp[n]
