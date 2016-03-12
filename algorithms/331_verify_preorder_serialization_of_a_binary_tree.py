class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        """
        Implementation 1: use stack (https://leetcode.com/discuss/83825/simple-python-solution-using-stack-with-explanation). when you see two consecutive "#" characters on stack, pop both of them and replace the topmost element on the stack with "#". 
        """
        # if not preorder:
        #     return False
        # stack = []
        # preorder = preorder.split(',')
        # for i in range(len(preorder)):
        #     stack.append(preorder[i])
        #     while len(stack) > 2 and stack[-2]=="#" and stack[-1]=="#":
        #         if stack[-3]=='#':
        #             return False
        #         else:
        #             stack.pop(-1)
        #             stack.pop(-2)
        # return True if stack == ["#"] else False
            
        """ 
    Implemetation 2: occupied slot (https://leetcode.com/discuss/84257/simplest-python-solution-with-explanation-stack-recursion). At the beginning, slots = 1 (root)
        "#" node: slots-=1
        other node: slot += (-1 + 2)
        """
        preorder = preorder.split(',')
        slot = 1
        for node in preorder:
            if slot == 0:
                return False
            if node == "#": 
                slot -= 1
            else:
                slot += 1
        return slot == 0
    
    
print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print Solution().isValidSerialization("1,#")
print Solution().isValidSerialization("9,#,#,1")
print Solution().isValidSerialization("1,#,#,#,#")
                