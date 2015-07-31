class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # # slow solution
    # def permuteUnique(self, nums):
    #     if len(nums)==0:
    #         return []
    #     else:
    #         result = self.permutation([[nums[0]]], nums[1:])
    #         return [list(x) for x in set(tuple(x) for x in result )]
    #     
    # def permutation(self, result, remain):
    #     if len(remain) == 0:
    #         return result
    #     else:
    #         res = []
    #         v = remain[0]
    #         for lst in result:
    #             for i in xrange(len(lst)+1):
    #                 new = lst[:i]+[v]+lst[i:]
    #                 res.append(new)
    #         return self.permutation(res, remain[1:])
    
    ### disscussion 
    # duplicates create when insert duplicated items before and after the same element
    # def permuteUnique(self, num):
    #     if not num:
    #         return []
    #     ret = [[]]
    #     for n in num:
    #         tmp = []
    #         l = len(ret[-1])
    #         for seq in ret:
    #             for i in range(l, -1, -1):
    #                 print seq, i, n
    #                 if i < l and seq[i] == n:
    #                     break
    #                 tmp.append(seq[:i] + [n] + seq[i:])
    #         ret = tmp
    #     return ret

    # modify my code, fast
    def permuteUnique(self, nums):
        if len(nums)==0:
            return []
        else:
            return self.permutation([[nums[0]]], nums[1:])
        
    def permutation(self, result, remain):
        if len(remain) == 0:
            return result
        else:
            res = []
            v = remain[0]
            for lst in result:
                l = len(lst)
                for i in xrange(len(lst), -1, -1):
                    if i < l and lst[i] == v:
                        break
                    new = lst[:i]+[v]+lst[i:]
                    res.append(new)
            return self.permutation(res, remain[1:])


print Solution().permuteUnique([1,1,2])
print Solution().permuteUnique([1,1,1,2,1])
print Solution().permuteUnique([3,3,0,0,2,3,2])