class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        longest = ""
        visited = {word: False for word in words}
        # leetcode compiler generates diff sorted output. 
        for word in sorted(words, key=lambda x: (len(x), reversed(x)), reverse=True):
            start = word[:-1]
            while len(start) >= 0 and start in visited and not visited[start]:
                if len(start) == 1 and len(longest) <= len(word):
                    longest = word
                visited[start] = True
                start = start[:-1]
        return longest

        words.sort()
        words.sort(key = len, reverse = True)
        for word in words:
            temp = word
            for i in range(1, len(temp)):
                if temp[:len(temp) - i] in words:
                    if i == len(temp) - 1:
                        return temp
                    continue
                else:
                    break
        return ''


print Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print Solution().longestWord(["rac","rs","ra","on","r","otif","o","onpdu","rsf","rs","ot","oti","racy","onpd"])
