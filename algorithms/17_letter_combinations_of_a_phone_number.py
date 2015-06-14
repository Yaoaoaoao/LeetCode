class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if digits == '':
            return []
        P = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        # letters = ['']
        # for i in list(digits):
        #     tmp = []
        #     for j in P[i]:
        #         for t in letters:
        #             tmp.append(t+j)
        #     letters = tmp
        # return letters
    
        
        # one-letter solution
        return reduce(lambda acc, digit: [x + y for x in acc for y in P[digit]], digits, [''])


print Solution().letterCombinations("23")