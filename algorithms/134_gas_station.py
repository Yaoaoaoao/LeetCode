class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        # discussion: because there is only one 
        # total gas should be more than cost gas. 
        # if A can't reach B, then any point between A and B can't reach B either.
        total, car = 0,0
        start = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            car += gas[i] - cost[i]
            if car < 0: 
                # can't reach i, reset the car gas and start point
                car, start = 0, -1
            else:
                # can travel to i, update the start point if start is -1
                if start == -1:
                    start = i
        return start if total >= 0 else -1

# print Solution().canCompleteCircuit([2], [2]) #0
print Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) #3