"""
Implement a prefix tree (Trie).
Key ideas: 
1. Each node has two attribute: children {Dict} and isWord {Boolean}.
2. Three operations: insert, search, and startsWith (a perfix)
3. O(m) for a word search (m is the length of the word). It's better than imperfect hash O(num_of_total_words).
"""
class TrieWord():
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieWord()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieWord()
            node = node.children[letter]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.findWord(word, 0, self.root)
        
    def findWord(self, word, idx, node): 
        if idx == len(word):
            return node.isWord
        letter = word[idx]
        if letter == '.':
            # Search every children, return True if any branch return True, else False. 
            for key in node.children.keys(): 
                if self.findWord(word, idx+1, node.children[key]):
                    return True
            return False
        elif letter in node.children:
            return self.findWord(word, idx+1, node.children[letter])
        else:
            return False


# wordDictionary = WordDictionary()
# wordDictionary.addWord("bad")
# wordDictionary.addWord("dad")
# wordDictionary.addWord("mad")
# print wordDictionary.search("pad")
# print wordDictionary.search("bad")
# print wordDictionary.search(".ad")
# print wordDictionary.search("b..")

# test = WordDictionary()
# test.addWord("a")
# test.addWord("ab")
# print test.search("a"),test.search("a."), test.search("ab"), test.search(".a"), test.search(".b"), test.search("ab."), test.search("."), test.search("..")
# [true,true,true,false,true,false,true,true]

t = WordDictionary()
t.addWord("at"),t.addWord("and"),t.addWord("an"),t.addWord("add")
print t.search("a"), t.search(".at")
t.addWord("bat")
print t.search(".at"), t.search("an."), t.search("a.d."), t.search("b."), t.search("a.d"), t.search(".")
# [false,false,
# true,true,false,false,true,false]