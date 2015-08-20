# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return '[%d,%d]' %(self.start, self.end)

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        # same way as the 56_merge_intervals.py, write in a different way
        # sort all intervals including newinterval
        # merge
        result = []
        intervals.append(newInterval)
        for i in sorted(intervals, key=lambda x:x.start):
            if result and i.start <= result[-1].end: # if not the first element and overlapping
                result[-1].end = max(result[-1].end, i.end)
            else: # not overlapping
                result.append(i)
        return result
            
            
        
print Solution().insert([Interval(s=1,e=3), Interval(s=6, e=9)],Interval(s=2, e=5)) #[1,5],[6,9]
print Solution().insert([Interval(s=1,e=2), Interval(s=3, e=5), Interval(s=6, e=7), Interval(s=8, e=10), Interval(s=12, e=16)], Interval(s=4, e=9)) #[1,2],[3,10],[12,16]
        