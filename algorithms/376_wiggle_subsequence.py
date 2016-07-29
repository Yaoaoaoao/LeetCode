class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Greedy: runtime O(2n)
        length = len(nums)
        if length <= 1:
            return length
        diff = [nums[i] - nums[i-1] for i in range(1, length)]
        i, j, result = 0, 1, 1
        if diff[0] != 0: 
            result += 1
        while j < length - 1:
            if diff[i] * diff[j] < 0:
                result += 1
                i = j
                j += 1
            else:
                j += 1
        return result
    
print Solution().wiggleMaxLength([1,7,4,9,2,5]) #6
print Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) #7
print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]) #2
print Solution().wiggleMaxLength([0]) #1
print Solution().wiggleMaxLength([0, 0]) #1
print Solution().wiggleMaxLength([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]) #67
