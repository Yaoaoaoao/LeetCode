"""
Every time 1-3 stones are removed. 
n=1: True
n=2: True
n=3: True
n=4: 1:F, 2:F, 3:F (means remove 1 stones at the first step, will lose the game )
n=5: 1-T, 2-F, 3-F
n=6: 2-T
n=7: 3-T
...
So if n=4,8,12... will lose the game, otherwise there is a way to win. 
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4==0 else True