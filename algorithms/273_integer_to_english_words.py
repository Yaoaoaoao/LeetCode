class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
        small = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        unit = ['', 'Thousand', 'Million', 'Billion']
        num = str(num)
        weight = 0
        right = len(num)
        result = []
        while right > 0:
            left = max(right-3, 0)
            fragment = int(num[left:right])
            fragmentWord = []
            hundred, remain = divmod(fragment, 100)
            if hundred > 0:
                fragmentWord.extend([small[hundred], 'Hundred'])
            if remain > 0:
                if remain <= 19:
                    fragmentWord.append(small[remain])
                else:
                    q, r = divmod(remain, 10)
                    fragmentWord.append(tens[q])
                    if r > 0:
                        fragmentWord.append(small[r])
            if len(fragmentWord) > 0:
                if weight > 0:
                    fragmentWord.append(unit[weight])
                result = fragmentWord + result
            right -= 3
            weight += 1
        return ' '.join(result)
            
print Solution().numberToWords(1234567) #One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
print Solution().numberToWords(0) 
print Solution().numberToWords(10000) 