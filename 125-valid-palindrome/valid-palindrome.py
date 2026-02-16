class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum(): #判断元素
                string.append(char.lower())

        return string[::-1] == string #翻转列表并对比
