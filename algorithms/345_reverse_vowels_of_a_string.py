class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Two pointer.
        VOWELS = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        left, right = 0, len(s)-1
        while left < right: 
            while left < right and s[left] not in VOWELS: 
                left += 1
            while left < right and s[right] not in VOWELS:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
    
print Solution().reverseVowels(" ")
print Solution().reverseVowels("a.")
print Solution().reverseVowels("aA")
print Solution().reverseVowels("hello")