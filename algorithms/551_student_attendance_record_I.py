class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return False
        absent, late_cont = 0, 0 
        # not more than one 'A' (absent) or more than two continuous 'L' (late)
        for i in s: 
            if i == 'A':
                absent += 1
                if absent > 1:
                    return False
                late_cont = 0
            elif i == 'L':
                late_cont += 1
                if late_cont > 2:
                    return False
            else:
                late_cont = 0
        return True


print Solution().checkRecord('PPALLP') == True
print Solution().checkRecord('PPALLL') == False
print Solution().checkRecord('') == False
