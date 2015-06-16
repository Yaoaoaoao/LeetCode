class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        # 2nd attemp # 112ms
        uniq = {}
        start, maxLen = 0, 0 
        for i in range(len(s)):
            if s[i] in uniq and start <= uniq[s[i]]:
                maxLen = max(maxLen, i-uniq[s[i]])
                start = uniq[s[i]] + 1
            else:
                maxLen = max(maxLen, i-start+1)
                
            uniq[s[i]] = i
                
        return maxLen
        
        # my 1st solution...  should use dict == 
        # 120ms
        s = list(s)
        unique, strlen = [], []
        for i in s:
            if i not in unique:
                unique.append(i)
            else:
                strlen.append(len(unique))
                unique = unique[unique.index(i)+1:]
                unique.append(i)
        strlen.append(len(unique))
        return max(strlen) if len(strlen) > 0 else 0
    
        # solution refine
        # 96ms
        unique = {}
        start, length = 0, 0
        for i in range(len(s)):
            if s[i] in unique and start <= unique[s[i]]:
                start = unique[s[i]] + 1
            else:
                length = max(length, i-start+1)
                
            unique[s[i]] = i # keep index
            
        return length
    
    
print Solution().lengthOfLongestSubstring('abcabcbb') # 3
print Solution().lengthOfLongestSubstring('bbbbbb') # 1
print Solution().lengthOfLongestSubstring('') # 0
print Solution().lengthOfLongestSubstring('c') # 1
print Solution().lengthOfLongestSubstring('abcd') #4
print Solution().lengthOfLongestSubstring('tmmzuxt') #5