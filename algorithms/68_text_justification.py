class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # this problem asks to use greedy alg
        
        # collect length of each word
        lens = [len(w) for w in words]
        # use greedy method to decide the beginning position of new line 
        current = 0 
        newline = [0]
        for l, l in enumerate(lens):
            if current + l > maxWidth:
                newline.append(l)
                current = 0
            current += l+1
        newline.append(len(words))
        
        # fill with spaces
        result = []
        for l in range(1, len(newline)):
            line = words[newline[l-1]:newline[l]]
            wordTotal = sum([len(w) for w in line])
            gap = len(line)-1
            space = maxWidth - wordTotal
            if len(line) == 1 or l == len(newline)-1: # one word line or last line
                result.append(' '.join(line)+' '*(space-gap)) 
            else:
                # new way
                minSpace = space//gap
                extraSpace = space%gap
                for i in range(0,len(line)-1):
                    line[i] += ' '*minSpace
                    if extraSpace>0:
                        line[i] += ' '
                        extraSpace -= 1
                # old way: slow
                # while extraSpace > 0:
                #     for i in range(len(line)-1):
                #         if extraSpace > 0:
                #             line[i] += ' '
                #             extraSpace -= 1
                result.append(''.join(line))
        return result
    
    
    
print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print Solution().fullJustify(["What","must","be","shall","be."], 12)