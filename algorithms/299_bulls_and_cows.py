class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # discussion
        from collections import Counter
        s, g = Counter(secret), Counter(guess)
        bull = sum(i == j for i, j in zip(secret, guess))
        return "%sA%sB" %  (bull, sum((s & g).values()) - bull )
        # 
        # 
        # bull, cow = 0, 0
        # n = len(secret)
        # unmatch_secret, unmatch_guess = [], []
        # for i in range(n):
        #     if secret[i] == guess[i]:
        #         bull += 1
        #     else:
        #         unmatch_secret.append(secret[i])
        #         unmatch_guess.append(guess[i])
        # for i in unmatch_secret:
        #     if i in unmatch_guess:
        #         cow += 1
        #         unmatch_guess.pop(unmatch_guess.index(i))
        # return "%dA%dB" % (bull, cow)
                
        
print Solution().getHint("1807", "7810") # 1A3B
print Solution().getHint("1123", "0111") # 1A1B
print Solution().getHint("1122", "2211") # 0A4B