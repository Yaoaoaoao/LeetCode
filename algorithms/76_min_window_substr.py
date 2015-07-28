class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        counter, counter_ = {}, {}
        n, n_ = len(t), 0
        result = ""
        # build counter dict
        for i in t:
            counter[i] = counter.get(i, 0) + 1
        begin = None
        for i in xrange(len(s)):
            if s[i] in counter:
                if begin is None:
                    begin = i
                counter_[s[i]] = counter_.get(s[i], 0) + 1
                if counter_[s[i]] <= counter[s[i]]:
                    n_ += 1
                if n_ == n:
                    # check from beginning, remove repeated t
                    while counter_[s[begin]] > counter[s[begin]]:
                        counter_[s[begin]] -= 1
                        begin += 1
                        while s[begin] not in counter:
                            begin += 1
                    # safe to extract string contain all t
                    str_ = s[begin:i+1]
                    if len(result)==0 or len(str_)<len(result):
                        result = str_

        return result
        
        
print Solution().minWindow("a", "a") # a
print Solution().minWindow("ab", "b") # b
print Solution().minWindow("bba", "ab") # ba
print Solution().minWindow("caae", "cae") # caae
print Solution().minWindow("ADOBECODEBANC", "ABC") #banc
print Solution().minWindow("ABCDEFGHIJKLMN", "OPQ") #
