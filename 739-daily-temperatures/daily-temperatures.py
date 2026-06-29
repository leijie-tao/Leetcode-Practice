class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # #brute force: iterate the lsit to find a higher temperature
        # n = len(temperatures)
        # res = [0] * n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             res[i] = j - i 
        #             break
        # return res

        
        #stack: Record the index, and add all waiting days into the satck.(descending order) Pop the element when find the higher temperature.(Last one is easier to find. ——> LIFO)
        n = len(temperatures)
        res = [0] * n
        stack = []  
        for i in range(n):
            #when stack has elements and the temperature is higher than the element, pop the last one.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)
        return res