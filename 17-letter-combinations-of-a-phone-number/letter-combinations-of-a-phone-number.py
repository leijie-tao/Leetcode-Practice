class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Create the map to look up
        phone = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"} 
        res = []
        path = []

        # Use index to locate the digit and look up for its characters
        def backtrack(index):
            # When path is full, add it to res
            if index == len(digits):
                res.append("".join(path))
                return
            
            # Get the list of all characters of current digits
            letters = phone[digits[index]]
            for char in letters: 
                path.append(char)
                backtrack(index+1)  # Move to the next digit
                path.pop()

        backtrack(0)
        return res

