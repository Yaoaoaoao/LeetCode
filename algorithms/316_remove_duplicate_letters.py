class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        https://leetcode.com/discuss/73777/easy-to-understand-iterative-java-solution
        find out the last appeared position for each letter
        find out the smallest index from the map in step 1 (a - 2)
        the first letter in the final result must be the smallest letter from index 0 to index 2;
        """
        result = ''
        while s:
            idx = min(map(s.rindex, set(s)))
            letter = min(s[:idx+1])
            result += letter
            s = s[s.index(letter):].replace(letter, '')
        return result
        
print Solution().removeDuplicateLetters("bcabc") # abc
print Solution().removeDuplicateLetters("cbacdcbc") # acdb