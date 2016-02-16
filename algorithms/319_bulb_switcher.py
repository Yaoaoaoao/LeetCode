class Solution(object):
    # find out how many factors a number has
    # 1!- 1
    # 2 - 1, 2
    # 3 - 1, 3
    # 4!- 1, 2, 4
    # 5 - 1, 5
    # 6 - 1, 2, 3, 6
    # 7 - 1, 7
    # 8 - 1, 2, 4, 8
    # 9!- 1, 3, 9
    # 10 - 1, 2, 5, 10
    # 12 - 1, 2, 3, 4, 6, 12
    # 16!- 1, 2, 4, 8, 16
    # only 1, 4, 9, 15, ..., n^2 have odds number of switch
    # the number of bulbs are on is sqrt(n)
    def bulbSwitch(self, n):
        return int(n**(0.5))
        
    # # Naive implement: Time Limit Exceeded 
    # def bulbSwitch(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     bulbs = [False] * n
    #     for r in range(1, n+1):
    #         for i in range(r-1, n, r):
    #             bulbs[i] = not bulbs[i]
    #     return bulbs.count(True)


print Solution().bulbSwitch(3) # 1
print Solution().bulbSwitch(10) # 3
print Solution().bulbSwitch(999999) # 999