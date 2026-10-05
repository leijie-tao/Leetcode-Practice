class Solution:
    def checkValidString(self, s: str) -> bool:
        # use low and high to record the number of unmatched '('
        low = high = 0
        for char in s:
            # meet '(' --> add one more unmatched '(' 
            if char == "(":
                low += 1
                high += 1
            # meet ')' --> match with ')', and decrease one more unmatched '('
            elif char == ")":
                low -= 1
                high -= 1
            # meet '*' --> take '*' as ')' or '(' ---> low: cost one unmatched "(".  high: get one unmatched '('.
            else:  # *
                low -= 1  
                high += 1
            
            # Result 1: all '*' as '(', but unmatched '(' aren't enough
            if high < 0: 
                return False
            # Result 2: all '*' as ')', get the number of unmatched '('
            low = max(low, 0)
        return low == 0 