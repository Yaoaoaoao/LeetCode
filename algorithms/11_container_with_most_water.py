class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        n = len(height)
        left, right, area = 0, n-1, 0
        while left < right:
            area = max(area, (right-left)* min(height[left], height[right]))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return area
    
print Solution().maxArea([3,1,2,4,5])
print Solution().maxArea([1,2,1])
    