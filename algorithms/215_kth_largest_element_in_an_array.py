from random import randint


class Solution(object):
    # # sort... O(nlgn)
    # def findKthLargest(self, nums, k):
    # return sorted(nums)[len(nums)-k]

    # randomized-select. divide-and-conquer O(n). 
    # select the n-k+1 th element ("sorted" from smallest to biggest)
    def findKthLargest(self, nums, k):
        n = len(nums)
        return self.randomized_select(nums, 0, n, n-k+1)

    def randomized_select(self, nums, p, r, i):
        """
        :param nums: 
        :param p: start
        :param r: end
        :param i: "k"
        :return:
        """
        if p == r: # only one element left
            return nums[p]
        q = self.randomized_partition(nums, p, r)
        k = q - p + 1
        if i == k: 
            # the pivot value is the answer
            return nums[q]
        elif i < k:
            return self.randomized_select(nums, p, q, i)
        else:
            return self.randomized_select(nums, q+1, r, i-k)

    def randomized_partition(self, nums, p, r):
        i = randint(p, r-1)
        nums[i], nums[r-1] = nums[r-1], nums[i]
        return self.partition(nums, p, r)

    def partition(self, nums, p, r):
        x = nums[r-1]
        i = p
        for j in range(p, r-1):
            if nums[j] <= x:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r-1] = nums[r-1], nums[i]
        return i


print Solution().findKthLargest([1], 1)  # 1
print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)  # 5
print Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],2)  # 10