class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums.sort(cmp=lambda x,y: cmp(x+y, y+x), reverse=True)
        return str(int(''.join(nums)))
    
# print Solution().largestNumber([3, 30, 34, 5, 9]) # 95343300
print Solution().largestNumber([0,0]) # 0