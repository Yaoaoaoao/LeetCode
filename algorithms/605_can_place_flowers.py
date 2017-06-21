class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flower = 0
        for i, f in enumerate(flowerbed):
            if f == 0:
                left = flowerbed[i - 1] if i > 0 else 0
                right = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
                if left == 0 and right == 0:
                    flowerbed[i] = 1
                    flower += 1
            if flower >= n:
                return True
        return False

print Solution().canPlaceFlowers([1,0,0,0,1], 1)
print Solution().canPlaceFlowers([1,0,0,0,1], 2)
print Solution().canPlaceFlowers([1,0,0,0,1,0,0], 2)