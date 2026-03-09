class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(":")","[":"]","{":"}"}
        stack = []
   
        for char in s:
            if char in d:
                stack.append(char) #左括号入栈
            else:
                if not stack:  #右括号过剩/先出现了右括号
                    return False
                left = stack.pop()
                if char != d[left]: #左右括号不匹配
                    return False

        return len(stack) == 0  #检测最后左括号是否多余

