class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: list[int]
        :rtype: list[int]
        """
        # Improvement: Use binary search to get the index
        if not nums:
            return []
        sort, result = [nums[-1]], [0]
        for n in range(len(nums)-2, -1, -1):
            idx = self.binary(sort, nums[n])
            result.insert(0, idx)
            sort.insert(idx, nums[n])
        return result
        
    def binary(self, array, target):
        start, end = 0, len(array)-1
        if array[end] < target:
            return end + 1
        if array[start] > target:
            return start
        while start < end:
            mid = (start+end)/2
            if array[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start
        
        # naive: start from the nth to 1st, maintain a sorted array. For ith element, 
        # the index it inserted into the sorted array is the answer. 
        # Time Limit Exceeded 
        if not nums:
            return []
        sort, result = [nums[-1]], [0]
        for n in range(len(nums)-2, -1, -1):
            idx = 0
            while idx < len(sort) and sort[idx] < nums[n]:
                idx += 1
            result.insert(0, idx)
            sort.insert(idx, nums[n])
        return result
        
print Solution().countSmaller([5,2,6,1]) # [2,1,1,0]
print Solution().countSmaller([5,7,6,8]) # [0,1,0,0]
print Solution().countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]) 
# [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]