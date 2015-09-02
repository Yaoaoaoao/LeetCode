class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1]+pascal[i-1][j])
            if i>0:
                row.append(1)
            pascal.append(row)
        return pascal
    
print Solution().generate(0)
print Solution().generate(1)
print Solution().generate(5)
print Solution().generate(10)