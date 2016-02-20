"""
idea: 
maintain two heaps:
small: smaller half of elements, max-heap, size n/2
large: bigger half of elements, min-heap, size n/2 (+ 1 if n is odd)
So the median is 
    large[0] if n is odd
    float(large[0]+small[0])/2 if n is even.

python heapq is Min-heap. The easiest way to get max-heap is invert all values.
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small = [] # Max-heap, all key are reversed
        self.large = [] # Min-heap

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.small or num > -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
            
        if len(self.small) > len(self.large):
            small_max = -heapq.heappop(self.small)
            heapq.heappush(self.large, small_max)
        if len(self.large) - len(self.small) > 1:
            large_min = heapq.heappop(self.large)
            heapq.heappush(self.small, -large_min)
        
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(-self.small[0] + self.large[0])/2.0
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
print mf.findMedian()
mf.addNum(2)
print mf.findMedian()
mf.addNum(3)
print mf.findMedian()
