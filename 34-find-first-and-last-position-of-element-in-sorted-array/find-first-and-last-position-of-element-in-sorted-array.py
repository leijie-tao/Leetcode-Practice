class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1  
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    bound = mid # 找到target暂时记录位置，但不确定是否是first/last
                    if isFirst:
                        right = mid - 1 # 找左边界(first)：继续往左找是否存在nums[mid]==target，并更新bound
                    else:
                        left = mid + 1  # 找右边界(last)：继续往右找，并更新bound
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return bound

        # 通过增加参数isFirst来决定找first/last，分别调用两次获取边界值
        start = findBound(True)
        end = findBound(False)
        
        return [start, end]
        