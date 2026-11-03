class Solution:
    # def numRescueBoats(self, people: list[int], limit: int) -> int:
    #     res = []
    #     people.sort()
    #     left, right = 0, len(people) - 1
    #     while left < right:
    #         while people[right] >= limit and right > 0:
    #             res.append(people[right])
    #             right -= 1 
    #         if people[left] + people[right] > limit:
    #             res.append(people[right])
    #             right -= 1
    #         else:
    #             res.append((people[left],people[right]))
    #             left += 1
    #             right -= 1

    #     if left == right:
    #         return len(res) + 1
    #     else:
    #         return len(res)


    def numRescueBoats(self, people: list[int], limit: int) -> int:
        res = []
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

                
