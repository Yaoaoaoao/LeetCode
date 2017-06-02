class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        from collections import Counter
        points = [p1, p2, p3, p4]
        c = Counter()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                c[self.length(points[i], points[j])] += 1
        
        return len(c.values()) == 2 and 4 in c.values() and 2 in c.values()
    
    def length(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        
        
        
        # sort points
        p = sorted([p1, p2, p3, p4], key=lambda x: x[0])
        if p[0][0] == p[1][0] and p[0][1] > p[1][1]:
            p[0], p[1] = p[1], p[0]
        if p[2][0] == p[3][0] and p[2][1] > p[3][1]:
            p[2], p[3] = p[3], p[2]
        
        # calculate length
        top_length = self.length(p[0], p[1])
        if top_length <= 0:
            return False
        bottom_length = self.length(p[2], p[3])
        if top_length != bottom_length:
            return False
        left_length = self.length(p[0], p[2])
        right_length = self.length(p[1], p[3])
        if left_length != right_length or left_length != top_length:
            return False

        # check slope: parallel
        top_slope = self.slope(p[0], p[1])
        bottom_slope = self.slope(p[2], p[3])
        if top_slope != bottom_slope:
            return False
        left_slope = self.slope(p[0], p[2])
        right_slope = self.slope(p[1], p[3])
        if left_slope != right_slope:
            return False

        # check verticle
        if top_slope[1] == 0:
            return left_slope[0] == 0
        if left_slope[1] == 0:
            return top_slope[0] == 0
        return top_slope[0] * left_slope[0] == -(top_slope[1] * left_slope[1])

    def length(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def slope(self, a, b):
        return (a[1] - b[1], a[0] - b[0])


print Solution().validSquare([0, 0], [1, 1], [1, 0], [0, 1])
print Solution().validSquare([1, 1], [4, 0], [2, 4], [5, 3])
print Solution().validSquare([1, 0], [-1, 0], [0, -1], [0, 1])
print Solution().validSquare([-658,-2922], [-965,-4209], [-2252,-3902], [-1945,-2615])
print Solution().validSquare([-1,1], [1,1], [1,-1], [-1,-1])