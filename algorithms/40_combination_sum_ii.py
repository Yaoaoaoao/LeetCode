class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        stack = [(0, -1, [])] # total, start, path
        result = []
        while stack:
            total, start, path = stack.pop(-1)
            if total == target and path not in result:
                result.append(path)
            for i in range(start+1, len(candidates)):
                total_ = total + candidates[i]
                if total_ > target:
                    break
                stack.append((total_, i, path+[candidates[i]]))
        return result
    
print Solution().combinationSum2([10,1,2,7,6,1,5], 8)