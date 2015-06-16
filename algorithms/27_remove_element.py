class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        count = 0
        for i in nums[:]:
            if i != val:
                count += 1
            else:
                nums.remove(i)
        return count
    
print Solution().removeElement([4,5], 4)