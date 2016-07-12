class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # If nums1 is smaller than nums2, switch them. 
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        # Sort two arrays. 
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        # two pointers.
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        intersection = []
        while i < m and j < n:
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
        return intersection
    
print Solution().intersect([1,2,2,1], [2,2])
        