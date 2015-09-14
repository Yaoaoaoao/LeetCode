class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height.append(0)
        area = 0
        stack = [0]
        for i in range(1, len(height)):
            # stack keeps a list of increasing height.
            # when height[i] is smaller than the last element of stack, remove stack element until the left
            # stack elements are smaller than height[i], the biggest area can be found by scanning elements
            # in the stack. each time, width = the stack value to the right i, height = current stack value
            while stack and height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                # current to the highest
                w = i if not stack else i-stack[-1]-1
                area = max(area, w*h)
            stack.append(i)
        return area
            
        

print Solution().largestRectangleArea([2,1,5,6,2,3])
print Solution().largestRectangleArea([1])
print Solution().largestRectangleArea([2,1,2])
print Solution().largestRectangleArea([4,2,0,3,2,5])
