class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # O(n)space
        l1, l2 = len(word1), len(word2)
        if l1==0 or l2==0:
            return l1+l2
        
        ### O(n) space
        dp = [0 for _ in range(l2+1)]
        for j in range(l2+1):
            dp[j] = j
        for i in range(1, l1+1):
            topleft = dp[0] # replace
            dp[0] += 1 
            for j in range(1, l2+1):
                left = dp[j] # insert
                if word1[i-1] == word2[j-1]:
                    dp[j] = topleft
                else:
                    dp[j] = min(dp[j-1], topleft, left)+1
                topleft = left
        return dp[-1]
            
        
        ### O(mn) space
        # A = [[0 for j in range(l2+1)] for i in range(l1+1)] #first is 0 match
        # # j=0
        # for i in range(1,l1+1):
        #     A[i][0] = i
        # # i=0
        # for j in range(1, l2+1):
        #     A[0][j] = j
        # # i>0 and j>0
        # for i in range(1, l1+1):
        #     for j in range(1, l2+1):
        #         if word1[i-1] == word2[j-1]:
        #             A[i][j] = A[i-1][j-1]
        #         else:
        #             A[i][j] = min(A[i][j-1], A[i-1][j], A[i-1][j-1])+1
        #             
        # return A[-1][-1]
    
print Solution().minDistance("", "") #0
print Solution().minDistance("ab", "bc") #2
print Solution().minDistance("hello", 'bell')#2
        
