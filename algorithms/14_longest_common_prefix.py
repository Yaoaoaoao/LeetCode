class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        for i, s in enumerate(zip(*strs)):
            if len(set(s))>1:
                return strs[0][:i]
        else:
            return min(strs)
            
            
    
print Solution().longestCommonPrefix(['aabbccd','aaaaaaa','aaaaa']) #aa