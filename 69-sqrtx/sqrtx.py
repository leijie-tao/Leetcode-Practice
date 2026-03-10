class Solution:
    def mySqrt(self, x: int) -> int:
        #brute force
        if x < 2:
            return x
        i = 2 #反向找结果
        while i * i <= x:
            i += 1
        
        return i -1