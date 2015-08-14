class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        p1, p2, end = m-1, n-1, m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1] > nums2[p2]:
                nums1[end] = nums1[p1]
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                p2 -= 1
            end -= 1
        # p2 has left over:
        while p2>=0:
            nums1[end] = nums2[p2]
            p2 -= 1
            end -= 1
    
print Solution().merge([1,3,5,7,9,11,13, None, None, None, None], 7, [2,4,6,8], 4)