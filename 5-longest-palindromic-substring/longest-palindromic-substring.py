class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        self.res = ""

        def extend(left, right):
            while left >= 0 and right < n and s[left] == s[right]: #The range limitation must be set first
                if (right - left + 1) > len(self.res): #Find longer substring. Then, update self.res
                    self.res = s[left:right+1]
                left -= 1
                right += 1
        
        for i in range(n):
            extend(i, i) #Odd length
            extend(i, i+1) #Even length

        return self.res