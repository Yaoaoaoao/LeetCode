class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type A: list[int]
        :type B: list[int]
        :rtype: float
        Runtime should be O(log(m+n)). -> binary search
        rank of median = (m+n)/2 if odd. 
        Nice explanation:
        https://leetcode.com/discuss/15790/share-my-o-log-min-m-n-solution-with-explanation
        Median: dividing a set into two equal length subsets, that one subset is always greater than the other
                  left_part          |        right_part
            A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
            B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
        
        Ensure: 
        1. len(left_part) == len(right_part)
        2. max(left_part) <= min(right_part)
        
        Two conditions:
        1.  i-1-0+1 + j-1-0+1 = m-1-i+1 + n-1-j+1
            i+j = m-i+n-j (+1 if odd) -> j = (m+n)/2 - i
        2. A[i-1] <= B[j] and B[j-1] <= A[i] 
            (and A[i-1] <= A[i] and B[j-1] <= B[j] because A and B are sorted)
            
        """
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        if n == 0:
            return None
            
        imin, imax = 0, m
        while imin <= imax:
            i = (imin+imax)/2
            j = (m+n+1)/2 - i
            
            if (j==0 or i==m or B[j-1] <= A[i]) and \
               (i ==0 or j ==n or A[i-1] <= B[j]):
                # find correct i
                if i == 0:
                    left_max = B[j-1]
                elif j == 0:
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1], B[j-1])

                if (m+n)%2 != 0:
                    return left_max

                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])

                return float(left_max + right_min)/2
            
            elif B[j-1] > A[i]:  # j need to move left, so increase i
                imin = i + 1
                
            elif A[i-1] > B[j]:  # i need to move left, so decrease i
                imax = i - 1
        
        
    """  
    # first: Navie O(m+n) method. Merge the two sorted list and calculate median
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        i, j = 0, 0
        all = []
        while i < m and j < n:
            if A[i] <= B[j]:
                all.append(A[i])
                i += 1
            else:
                all.append(B[j])
                j += 1
        all.extend(A[i:])
        all.extend(B[j:])
        median = int((m+n-0.5)/2)
        if (m+n)%2 != 0: # odd
            return all[median]
        else: # even
            return float(all[median] + all[median+1])/2
    """
        
        
            
            
print Solution().findMedianSortedArrays([1,3,5,7,9], [2,4,6,8] ) # 5
print Solution().findMedianSortedArrays([1,3,5,7], [2,4,6,8] ) # 4.5
print Solution().findMedianSortedArrays([], [1,2,3,4,5] ) # 3
            
        