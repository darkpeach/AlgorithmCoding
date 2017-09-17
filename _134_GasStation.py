class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        diff = []
        for i in xrange(length):
            diff.append(gas[i] - cost[i])
        for i in xrange(length):
            diff.append(gas[i] - cost[i])
        for start in xrange(0, length):
            if diff[start] < 0:
                continue
            total = 0
            now = start
            while total >= 0 and now < start + length:
                total += diff[now]
                now += 1
            if now == start + length and total >= 0:
                return start
        return -1