class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # brute-force O(dict * words)
        # trie
        trie = {}
        for word in dict:
            t = trie
            for w in word:
                if not w in t:
                    t[w] = {}
                t = t[w]
            t[''] = word

        def find_root(word):
            t = trie
            for letter in word:
                if letter in t:
                    t = t[letter]
                    if '' in t:
                        return t['']
                else:
                    break
            return word

        words = sentence.split(' ')
        for i in range(len(words)):
            words[i] = find_root(words[i])
        return ' '.join(words)


# print Solution().replaceWords(["cat", "bat", "rat"],
#                               "the cattle was rattled by the battery")
print Solution().replaceWords(["a", "aa", "aaa", "aaaa"],
                              "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa")
