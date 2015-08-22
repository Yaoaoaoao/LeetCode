class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        add = 1
        for i in reversed(digits):
            d = add+i
            add = d//10
            result.append(d%10)
        if add:
            result.append(add)
        result.reverse()
        return result
                
print Solution().plusOne([0])
print Solution().plusOne([9,9,9])