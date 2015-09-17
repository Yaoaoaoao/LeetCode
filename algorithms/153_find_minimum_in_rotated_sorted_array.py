class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case: len=0, len=1, already sorted
        if not nums:
            return None
        left, right = 0, len(nums)-1
        minValue = nums[0]
        while left <= right:
            if nums[left]<=nums[right]:
                minValue = min(minValue, nums[left])
                break
            mid = (left+right)//2
            if nums[left] > nums[mid]: # 671-2-345 56-1-234
                right = mid - 1
                minValue = min(minValue, nums[mid])
            elif nums[right] < nums[mid]: # 345-6-712 34-5-612
                left = mid + 1
                minValue = min(minValue, nums[right])
        return minValue
