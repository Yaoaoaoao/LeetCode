class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        O(nlgn) solution. 
        First thought: this is the form of binary search. 
        Which part is wasting time in naive solution? When we update the lis list, every number ahead of the element 
        needs to be checked. If we know which number has the highest count and compare the element with it?, we can 
        save a lot of time. - If the highest count doesn't work, use binary search to find the desired count. The runtime
        should be O(n) to loop through each element plus O(nlgn) worst time to find the highest count. 
        Explanation: https://discuss.leetcode.com/topic/28757/c-o-nlogn-solution-with-explainations-4ms/2
        """
        if len(nums) == 0:
            return 0
        lis = []
        for num in nums:
            pos = self.find_last_smallest_pos(lis, num)
            if pos == len(lis):
                lis.append(num)
            else:
                lis[pos] = min(lis[pos], num)
        return len(lis)
        
    def find_last_smallest_pos(self, lis, num):
        if len(lis) == 0:
            return 0
        start, end = 0, len(lis)
        while start < end:
            mid = (start + end) / 2
            if lis[mid] < num:
                start = mid + 1
            else:
                end = mid
        return start

        """
        Naive O(n**2) solution.
        Use lis to track the longest increasing subsequence. 
        lis[x] = y means there is a lis of length y for the subarray nums[0:x+1]. 
        For the element x+1, compare with every element ahead of it and update the maximum lis.
        """
        if len(nums) == 0:
            return 0
        lis = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)
        return max(lis)


print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])
print Solution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
