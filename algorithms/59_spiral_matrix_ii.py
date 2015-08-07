class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        # my 60ms solution
        # if n == 0:
        #     return []
        # matrix = [[n**2]]
        # num = n**2-1
        # while num>0:
        #     for i in matrix:
        #         i.insert(0, num)
        #         num -= 1
        #     # last line
        #     matrix.append(range(num, num-len(matrix[0]), -1))
        #     num -= len(matrix[0])
        #     if num>0: # odd
        #         for i in range(len(matrix[-1])-1, -1, -1):
        #             matrix[i].append(num)
        #             num -= 1
        #         # first lines
        #         matrix.insert(0, range(num-len(matrix[-1])+1, num+1))
        #         num -= len(matrix[-1])
        #     else: # even
        #         matrix = [m[::-1] for m in matrix[::-1]]
        # return matrix

        # discussion 48ms solution
        matrix = []
        num = n**2+1
        while num > 1: 
            num, right = num - len(matrix), num
            matrix = [range(num, right)] + zip(*matrix[::-1])
        return matrix

        
    
print Solution().generateMatrix(0)
print Solution().generateMatrix(2)
print Solution().generateMatrix(3)
print Solution().generateMatrix(5)