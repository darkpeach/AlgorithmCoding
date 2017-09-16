class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for start in range(0, len(gas)):
            total = 0
            flag = 0
            for station in range(start, len(gas)):
                total += gas[station]
                if total < cost[station]:
                    break
                else:
                    total -= cost[station]
                    flag += 1
            else:
                for station in range(0, start):
                    total += gas[station]
                    if total < cost[station]:
                        break
                    else:
                        total -= cost[station]
                        flag += 1

            if flag == len(gas):
                return start
        return -1