class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # slow 256 ms solution
        from collections import defaultdict
        grp = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            grp[key].append(s)
        return [sorted(v) for v in grp.values()]
    
print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])