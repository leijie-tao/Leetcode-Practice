class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search: Find the target speed between min_speed and max_speed
        min_speed = 1
        max_speed = max(piles)

        while min_speed <= max_speed:
            mid = min_speed + (max_speed - min_speed) // 2
            #Calculate the hours needed for finishing all the piles
            hours_need = 0
            for pile in piles:
                hours_need += math.ceil(pile / mid)         #math.ceil() is round up to an integer

            if hours_need <= h:     #Notice: Don't stop when ==. Need to find the minimum integer.
                max_speed = mid - 1
            else:
                min_speed = mid + 1

        return min_speed