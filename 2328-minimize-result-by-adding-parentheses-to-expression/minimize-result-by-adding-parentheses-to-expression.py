class Solution:
    def minimizeResult(self, expression: str) -> str:
        # Split string with +
        min_res = float('inf')
        plus_index = expression.index('+')
        n = len(expression)
        
        # Loop through the string from two sides
        for i in range(plus_index):
            for j in range(plus_index + 1, n):
                # Add parentheses into the string
                expr = expression[:i] + "(" + expression[i:j+1] + ")" + expression[j+1:]
                a = expression[:i]
                b = expression[i:plus_index]
                c = expression[plus_index+1:j+1]
                d = expression[j+1:]
                
                # Calculate the value of sliced strings, and update the result string
                val = (int(a) if a else 1) * (int(b) + int(c)) * (int(d) if d else 1)
                if val < min_res:
                    min_res = val
                    res = expr
        return res

