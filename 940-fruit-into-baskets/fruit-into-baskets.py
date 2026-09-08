class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        left = right = 0
        window = defaultdict(int)
        res = 0

        # Right pointer to explore elements that can be added into bucket
        for right in range(n):
            window[fruits[right]] += 1
            # len(window) is the number of the bucket ----> fixed window size
            while len(window) > 2:
                window[fruits[left]] -= 1
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                left += 1
            res = max(res, right - left + 1)

        return res