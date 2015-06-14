class Solution:
    """
    zigzag pattern is |/|/|/.....
    """
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        # my solution: 120ms
        if numRows == 1:
            return s
        l, slash, ans = len(s), numRows-2, ''
        bar = numRows*2-2 # may equal 0 
        for row in range(numRows):
            x = 0
            if row == 0:
                while bar * x < l:
                    ans += s[bar * x]
                    x += 1
            elif row == numRows - 1:
                while bar * x + numRows - 1 < l:
                    ans += s[bar * x + numRows - 1 ]
                    x += 1
            else:
                while bar * x + row < l:
                    ans += s[bar * x + row]
                    if bar * x + numRows - 1 + slash < l:
                        ans += s[bar * x + numRows - 1 + slash]
                    x += 1
                slash -= 1
        return ans
            
        # other's solution: 124 ms
        if numRows == 1:
            return s
        cycle = numRows*2-2
        lines=["" for i in range(numRows)]
        # index number : line number
        d = {i:i if i < numRows else cycle-i for i in xrange(cycle)}
        # set each character to line
        for i in xrange(len(s)):
            lines[ d[i%cycle] ] += s[i]
        return ''.join(lines)
        
    
print Solution().convert("A", 1)
print Solution().convert('PAYPALISHIRING', 3) #PAHNAPLSIIGYIR
print Solution().convert('ABCDEFGHIJKLMNOPQRSTU', 5) #AIQBHJPRCGKOSDFLNTEMU