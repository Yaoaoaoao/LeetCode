class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # O(nlog(n)*log(n))
        n = len(matrix)
        left, right = matrix[0][0], matrix[n-1][n-1]
        while left < right:
            middle = (left + right) / 2 
            # Count how many numbers are smaller than the middle. 
            countSmall = 0
            for i in range(n):
                row = matrix[i]
                rowLeft, rowRight = 0, n
                while rowLeft < rowRight:
                    rowMid = (rowLeft + rowRight) / 2 
                    if row[rowMid] > middle:
                        rowRight = rowMid
                    else:
                        rowLeft = rowMid + 1
                countSmall += rowLeft
            if countSmall >= k:
                right = middle
            else:
                left = middle + 1
        return left
                
            
        
print Solution().kthSmallest([
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8)