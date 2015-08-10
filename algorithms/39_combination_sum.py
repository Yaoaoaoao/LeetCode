class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        # dfs solution
        # stack = [(total, start, path)]
        candidates = sorted(candidates)
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, path = stack.pop(-1)
            if total == target:
                result.append(path)
            for i in range(start, len(candidates)):
                total_ = total + candidates[i]
                if total_ > target:
                    break
                stack.append((total_, i, path+[candidates[i]]))
        return result
    
print Solution().combinationSum([2,3,6,7], 7)
print Solution().combinationSum([8,7,4,3], 11) #[[3,4,4],[3,8],[4,7]]