class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for move in list(moves):
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
        return x == 0 and y == 0
    
print Solution().judgeCircle("UD")
print Solution().judgeCircle("LL")
print Solution().judgeCircle("LDRRLRUULR") # false