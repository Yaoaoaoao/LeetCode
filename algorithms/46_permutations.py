class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    # def permute(self, nums):
    #     if len(nums)==0:
    #         return []
    #     return self.permutation([[nums[0]]], nums[1:])
    #         
    # def permutation(self, result, remain):
    #     if len(remain) == 0:
    #         return result
    #     else:
    #         res = []
    #         v = remain[0]
    #         for l in result:
    #             for i in xrange(len(l)+1):
    #                 # new = l[:]
    #                 # new.insert(i, v)
    #                 new = l[:i]+[v]+l[i:]
    #                 res.append(new)
    #         return self.permutation(res, remain[1:])

    def permute(self, nums):
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
        return perms

print Solution().permute([1,2,3])