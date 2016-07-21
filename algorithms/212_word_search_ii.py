class Solution(object):
    def __init__(self):
        self.trie = None
        self.board = []
        self.n = 0
        self.m = 0
        self.result = set()

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        """
        Build a Trie for words. Use dfs to search the board. 
        """
        self.trie = self.buildTrie(words)
        self.board = [list(i) for i in board]
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(i, j, self.trie, "")
        return list(self.result)

    def buildTrie(self, words):
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['isWord'] = True
        return trie

    def dfs(self, i, j, node, word):
        if 'isWord' in node:
            self.result.add(word)
        if i < 0 or i == self.n or j < 0 or j == self.m or self.board[i][j] not in node:
            return
        letter = self.board[i][j]
        self.board[i][j] = "#"
        word += letter
        self.dfs(i - 1, j, node[letter], word)
        self.dfs(i + 1, j, node[letter], word)
        self.dfs(i, j - 1, node[letter], word)
        self.dfs(i, j + 1, node[letter], word)
        self.board[i][j] = letter


print Solution().findWords(["ab", "cd"], ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb",
                                          "acb"])  # ["ab","ac","bd","ca","db"]
print Solution().findWords(["a"], ["a"])  # a
print Solution().findWords(["aa"], ["a"])  # a
print Solution().findWords(["ab"], ["ba"])  # ba
print Solution().findWords(["aa"], ["aaa"])  # []
print Solution().findWords(["ab", "aa"],
                           ["aba", "baa", "bab", "aaab", "aaa", "aaaa", "aaba"])  # ["aaa","aaab","aaba","aba","baa"]
