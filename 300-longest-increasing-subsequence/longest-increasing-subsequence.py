class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(res, n):
            left, right = 0, len(res) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        for n in nums:
            if not res or res[-1] < n:  #如果递增，则把当前元素添加至res
                res.append(n)
            else:   #不是递增，则在res中寻找一个位置（刚大于n），把该位置的数替换为n
                idx = binary_search(res, n)
                res[idx] = n
                
        return len(res)
