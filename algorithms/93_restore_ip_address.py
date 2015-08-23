class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return ['.'.join(s) for s in self.restore(s, [])] if len(s) > 0 else []
        
    def restore(self, s, address):
        if len(s) == 0:
            return [address] if len(address) == 4 else []
        elif len(s) > 0 and len(address) >= 4:
            return []
        else:
            result = []
            for i in range(1, min(len(s), 3)+1):
                part = s[0:i]
                partInt = int(part)
                if part[0] == '0' and len(part) > 1: # 00 or 0x or 0xx are invalid
                    continue
                if 0 <= partInt <= 255:
                    tmp = self.restore(s[i:], address+[part])
                    for t in tmp:
                        result.append(t)
            return result

print Solution().restoreIpAddresses("")
print Solution().restoreIpAddresses("25525511135")
print Solution().restoreIpAddresses("010010") # ["0.10.0.10","0.100.1.0"]