class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #General: compare the sum value and return -1 if the traveling is completely impossible
        if sum(gas) < sum(cost):
            return -1
        
        
        start = 0
        tank = 0
        n = len(gas)
        for i in range(n):
            tank += gas[i] - cost[i]    #Update tank at current station
            #Greedy: if gas run out at any station i, all the stations between the start and i can't be the valid start.
            if tank < 0:
                start = i + 1   #We can only start from the station after i+1
                tank = 0        #And reset tank
        return start

