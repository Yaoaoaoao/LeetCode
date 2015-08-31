class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left, right = 0, len(height)-1
        leftmax, rightmax = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax-height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax-height[right]
                right -= 1
        return water
                
        
    
print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) #6