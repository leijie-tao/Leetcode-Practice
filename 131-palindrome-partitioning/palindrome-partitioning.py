class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)

        def backtrack(start):
            # All substring success, `start` can reach to n
            if start == n:
                res.append(path[:])
            # end restrains the length of substring (1 ~ n). Try cut 1 character/ 2 characters ... n characters
            for end in range(start + 1, n + 1):
                segment = s[start:end]
                # Add palindrome into path ---> recursion --> if fail, pop & backtrack
                if segment == segment[::-1]:
                    path.append(segment)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res
