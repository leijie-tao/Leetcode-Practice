class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] #Record the min_val so far.  The later, the smaller.

    def push(self, value: int) -> None:
        self.stack.append(value)
        # If min_stack is empty or find a smaller value, add the value into min_stack.
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        # If the removed element is the minimum, remove it from min_stack as well.
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()        
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()