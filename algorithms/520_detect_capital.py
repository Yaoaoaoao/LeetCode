class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        first = self.check(word[0])
        if first == 'c':
            second = self.check(word[1])
            if second == 'c':
                return self.checkWord(word[1:], 'c')
            elif second == 'l':
                return self.checkWord(word[1:], 'l')
            else:
                return False

        elif first == 'l':
            return self.checkWord(word[1:], 'l')
        else:
            return False

    def checkWord(self, w, target):
        for i in w:
            if self.check(i) != target:
                return False
        return True

    def check(self, l):
        # A-Z:65-90 a-z:97-122
        if 65 <= ord(l) <= 90:
            return 'c'
        elif 97 <= ord(l) <= 122:
            return 'l'
        return False

print Solution().detectCapitalUse("USA")
print Solution().detectCapitalUse("FlaG")
print Solution().detectCapitalUse("Google")