# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda x: x.start)
        result = []
        for interval in intervals:
            if result != [] and result[-1].end >= interval.start:
                result[-1].end = max(result[-1].end, interval.end)
            else:
                result.append(interval)
        return result