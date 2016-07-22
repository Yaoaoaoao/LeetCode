class Solution(object):
    # def maxProduct(self, words):
    #     """
    #     :type words: List[str]
    #     :rtype: int
    #     """
    #     """
    #     1. all possible subset of size 2
    #     2. share common letter
    #     3. maximum sum
    #     Naive O(n^2) -> Time Limit Exceeded
    #     """
    #     numOfWords = len(words)
    #     maxProduct = 0
    #     for i in range(numOfWords-1):
    #         for j in range(1, numOfWords):
    #             product = len(words[i]) * len(words[j])
    #             if product < maxProduct: 
    #                 continue
    #             if not self.shareCommonLetter(words[i], words[j]):
    #                 maxProduct = max(product, maxProduct)
    #     return maxProduct                
    #     
    # def shareCommonLetter(self, word1, word2):
    #     return len(set(list(word1)).intersection(set(list(word2)))) != 0

    """
    Improvement: enumerate all subsets are too slow. 
    Sorted the listed by word length, started from the longest word. 
    Sort O(nlgn) - Best time, then loop through the list -> worst time is still O(n^2)
    
    Simple improvement: calculate product, if current product is smaller than maxProduct
    continue without checking common letter. 
    
    Bit manipulation: Use 26 bits of 32-integer. If a letter is presented in the word, the correspond bit is 1.
    int bitwise and int = 1 means no shared letter. 
    """

    def maxProduct(self, words):
        numOfWords = len(words)
        preprocess = [0] * numOfWords
        for i in range(numOfWords):
            for letter in words[i]:
                preprocess[i] |= 1 << (ord(letter) - ord('a')) # 1 << offset: move 1 to the offset (position)
        maxProduct = 0
        for i in range(numOfWords-1):
            for j in range(1, numOfWords):
                if not preprocess[i] & preprocess[j]:
                    product = len(words[i]) * len(words[j])
                    maxProduct = max(product, maxProduct)
        return maxProduct