class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 52ms
        if not matrix or target is None:
            return False
        
        row, col = len(matrix), len(matrix[0])
        lo,hi = 0, row*col-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            m = matrix[mid//col][mid%col]
            if m == target:
                return True
            elif m > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
            
            
    # # 60 ms
    # def searchMatrix(self, matrix, target):
    #     if not len(matrix) or not len(matrix[0]): 
    #         return False
    #     # use binary search to find the correct row
    #     row = self.binary([i[0] for i in matrix], target)
    #     # use binary search to find the element in the row
    #     col = self.binary(matrix[row], target)
    #     return True if matrix[row][col]==target else False
    #     
    # def binary(self, list, target):
    #     if len(list) == 0:
    #         return False
    #     lo, hi = 0, len(list)
    #     while lo < hi:
    #         mid = (hi+lo)//2
    #         if target < list[mid]:
    #             hi = mid
    #         elif target > list[mid]:
    #             lo = mid +1
    #         else:
    #             return mid
    #     return lo-1 # can't find
        
print Solution().searchMatrix([], 0) #f
print Solution().searchMatrix([[1,1]], 2) #f
print Solution().searchMatrix([[1,3]], 3) #t
print Solution().searchMatrix([[1,3,5]], 5) #t
print Solution().searchMatrix([
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 1)