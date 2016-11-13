class Solution(object):
  def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    if len(p) > len(s):
      return []
    
    result = []
    p_profile = [0 for _ in range(26)]
    for i in map(lambda x: self.index(x), list(p)):
      p_profile[i] += 1

    # load prevous p-1 character to profile.
    s_profile = [0 for _ in range(26)]
    for i in range(len(p) - 1):
      s_profile[self.index(s[i])] += 1

    # sliding window from the p-1 th position. Add the pth character in profile,
    # compare two profiles, add begin index to result if match, remove the first
    # character from the profile. 
    for end in range(len(p) - 1, len(s)):
      begin = end - len(p) + 1
      s_profile[self.index(s[end])] += 1
      if self.compare(s_profile, p_profile):
        result.append(begin)
      s_profile[self.index(s[begin])] -= 1
    
    return result

  def index(self, a):
    return ord(a) - 97

  def compare(self, a, b):
    for i in range(26):
      if a[i] != b[i]:
        return False
    return True

    # # naive: time exceeds
    # def findAnagrams(self, s, p):
    #   result = []
    #   window_size = len(p)
    #   for i in xrange(len(s)-window_size+1):
    #     if self.is_anagrams(s[i:i+window_size], p):
    #       result.append(i)
    #   return result
    # 
    # def is_anagrams(self, a, b):
    #   return sorted(a) == sorted(b)


print Solution().findAnagrams("cbaebabacd", "abc") # [0,6]
print Solution().findAnagrams("abab", "ab") # [0,1,2]
