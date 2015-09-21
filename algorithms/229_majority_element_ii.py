class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
         Find majority element (# > 2/n)
         Boyer-Moore Algorithm:
         http://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
         candidate, count = 0, 0 
         for nums in nums:
            if count == 0:
                candidate = num
            if cadidate == num:
                count += 1
            else:
                count -= 1
        '''
        if not nums:
            return []
        candidate1, candidate2, count1, count2 = None,None,0,0
        for num in nums:
            if count1 == 0:
                candidate1, count1 = num, 1
            elif candidate1 == num:
                count1 += 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            elif candidate2 == num:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        result = {candidate1: 0, candidate2: 0}
        for num in nums:
            if num in result:
                result[num] += 1
        return [k for k,v in result.iteritems() if k!=None and v > len(nums)//3]



print Solution().majorityElement([1])
print Solution().majorityElement([1,1,1,2,2,2,3,3])