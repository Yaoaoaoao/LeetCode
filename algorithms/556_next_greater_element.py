class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Next permutation
        nums = list(str(n))
        l = len(nums)
        i = l - 2
        # Find the pivot to swap: first left < right.
        while i >= 0 and nums[i] >= nums[i + 1]: 
            i -= 1
        # No result.
        if i < 0:
            return -1
        # Find the furthest number that is greater than nums[i].
        j = l - 1
        while nums[i] >= nums[j]:
            j -= 1
        # Swap.
        nums[i], nums[j] = nums[j], nums[i]
        # Reverse the string from pivot to end (since it's in descending order).
        a, b = i + 1, l - 1
        while a < b:
            nums[a], nums[b] = nums[b], nums[a]
            a += 1
            b -= 1

        res = int(''.join(nums))
        return -1 if res > 2147483647 else res


print Solution().nextGreaterElement(1234)
print Solution().nextGreaterElement(21)
print Solution().nextGreaterElement(1253421)
print Solution().nextGreaterElement(1999999999) # -1
