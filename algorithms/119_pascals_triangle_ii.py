class Solution(object):
    # discussion:
    # 64ms
    def getRow(self, rowIndex):
        result = [1] + [0]*rowIndex
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                result[j] += result[j-1]
        return result
                
    
    # # my 52ms
    # def getRow(self, rowIndex):
    #     """
    #     :type rowIndex: int
    #     :rtype: List[int]
    #     """
    #     half = [1]
    #     rowIndex += 1
    #     if rowIndex == 1:
    #         return half
    #     for row in range(2, rowIndex+1):
    #         half.append(half[-1])
    #         tmp = [half[0]]
    #         for i in range(1, (row+1)//2):
    #             tmp.append(half[i-1]+half[i])
    #         half = tmp
    #     if rowIndex%2==0:
    #         return half+list(reversed(half))
    #     else:
    #         return half+list(reversed(half[:-1]))
    
    
print Solution().getRow(2)
print Solution().getRow(3)
print Solution().getRow(4)
print Solution().getRow(5)
            
    
