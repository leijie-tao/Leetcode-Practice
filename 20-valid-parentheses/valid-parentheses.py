class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {"(":")", "[":"]", "{":"}"}
        for o in s:
            if o in map:
                stack.append(o)
            else:
                # check if the left parts are enough to pop
                if len(stack) == 0:
                    return False
                #check if it's a valid pair
                tmp = stack.pop()
                if map[tmp] != o:
                    return False
        # check if left parts are all paired
        if len(stack) == 0:
            return True
        else:
            return False

