# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __repr__(self):
        return '[%d,%d]' %(self.start, self.end)

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        # sort by the first element
        intervals = sorted(intervals, key=lambda x: x.start)
        # check if overlap
        last = None
        result = []
        for i in intervals:
            if last is None:
                result.append(Interval(s=i.start))
                last = i.end
                continue
            if i.start <= last: # overlap
                last = max(last, i.end)
            else:   # not overlapp
                result[-1].end = last
                result.append(Interval(s=i.start))
                last = i.end
        result[-1].end = last
        return result
        
print Solution().merge([Interval(s=1,e=3), Interval(s=2, e=6),Interval(s=8, e=10), Interval(s=15, e=18)])
print Solution().merge([Interval(s=1,e=4), Interval(s=2, e=3)])