class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # follow idea of https://discuss.leetcode.com/topic/80056/python-o-n
        # -solution-with-visual-explanation/6
        # O(n)
        count = {0: -1}
        sum_, longest = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sum_ -= 1
            else:
                sum_ += 1
            if sum_ in count:
                longest = max(longest, i - count[sum_])
            else:
                count[sum_] = i
        return longest

        # O(n^2)
        l = len(nums)
        sum_ = [0]
        for i in range(1, l + 1):
            sum_.append(sum_[i - 1] + nums[i - 1])
        longest = 0
        for i in range(l + 1):
            for j in range(i + 1, l + 1):
                if (sum_[j] - sum_[i]) * 2 == j - i:
                    longest = max(longest, j - i)
        return longest


print Solution().findMaxLength([0, 1])
print Solution().findMaxLength([0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0])
