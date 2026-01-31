class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"} #回溯与哈希表结合
        res = []
        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path)) #把path(list)里的元素连接起来，整体作为元素放入res
                return
            letters = phone[digits[index]] #根据哈希表定位字母串
            for char in letters: #遍历index位的每个字母
                path.append(char)
                backtrack(index+1, path) #index位的字母与index+1位的字母组合
                path.pop()

        backtrack(0, [])
        return res

