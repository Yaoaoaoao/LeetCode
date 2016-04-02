class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: list[int]
        """
        if not num >= 0:
            return []
        result = [0]
        power = 1
        for i in range(1, num+1):
            if power * 2 == i:
                power *= 2
            result.append(result[i-power] + 1)
        return result
            

print Solution().countBits(5) # [0, 1, 1, 2, 1, 2]
print Solution().countBits(16) # [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]


