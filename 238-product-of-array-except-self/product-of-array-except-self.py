class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # brute force: Find the array except self & Calculate the product
        # res = []
        # for i in range(len(nums)):
        #     temp = nums[: i] + nums[i+1 :]
        #     product = 1
        #     for t in temp:
        #         product *= t
        #     res.append(product)
        # return res



        # Method 2: divide the array into 2 parts (left & right)
        n = len(nums)
        left = [1] * n
        right = [1] * n

        #Left part: for who has left part
        for i in range(1, n): 
            left[i] = left[i-1] * nums[i-1]
        #Right part: for who has rihgt part (direction: right to left)
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        #Multiply left part with right part to get the result
        res = []
        for i in range(n):
            res.append(left[i] * right[i])
        return res
        