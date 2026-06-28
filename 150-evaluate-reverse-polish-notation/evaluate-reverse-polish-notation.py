class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            # If it's an operator, pop 2 numbers to calculate.
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)         #Notice: the order matters
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))    #Notice: the order matters
            # If it's a number, add it into the stack.
            else:
                stack.append(int(t))

        return stack[-1]