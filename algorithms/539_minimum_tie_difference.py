class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        circle = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            circle.append(h * 60 + m)
        circle = sorted(circle)  # nlogn
        min_diff = 1440
        for i in range(len(circle)):
            d = abs(circle[i] - circle[i - 1])
            if d > 720:
                d = min(abs(0 - circle[i]), 1440 - circle[i]) + min(
                    abs(0 - circle[i - 1]), 1440 - circle[i - 1])
            min_diff = min(min_diff, d)
        return min_diff


print Solution().findMinDifference(["23:59", "00:00", "01:00"])
