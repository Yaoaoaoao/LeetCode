"""
Binary Indexed Trees (BIT or Fenwick tree)
https://leetcode.com/discuss/74222/java-using-binary-indexed-tree-with-clear-explanation
         8
     4
   2   6
0 1 3 5 7
b[1] = a[0]
b[2] = a[1]+b[1] = a[1]+a[0]
b[3] = a[2]
b[4] = a[3]+b[3]+b[2] = a[3]+a[2]+a[1]+a[0]
b[5] = a[4]
b[6] = a[5]+b[5] = a[5]+a[4]
b[7] = a[6]
b[8] = a[7]+b[7]+b[6]+b[4] = a[7]+a[6]+a[5]+a[4]+a[3]+a[2]+a[1]+a[0]

x & -x is the lowbit function. It will return x's rightmost one bit. 

initialize: O(nlgn)
update: O(lgn)
query: O(lgn) = 2*lgn
space: O(n)
"""


class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.length = len(nums)
        self.prefix_sum = [0] * (self.length + 1)
        for i in range(self.length):
            self.update_bit(i + 1, nums[i])

    def update_bit(self, k, value):
        # e.g. when i = 1
        # update b[2], b[4], b[8]
        while k <= self.length:
            self.prefix_sum[k] += value
            k += (k & -k)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.update_bit(i + 1, diff)

    def get_sum(self, k):
        sum = 0
        k += 1
        while (k > 0):
            sum += self.prefix_sum[k]
            k -= (k & -k)
        return sum

    def sumRange(self, i, j):
        return self.get_sum(j) - self.get_sum(i-1)


    # runtime error

# class NumArray(object):
# def __init__(self, nums):
# self.nums = nums
# 
#     def update(self, i, val):
#         self.nums[i] = val
# 
#     def sumRange(self, i, j):
#         return reduce(lambda x,y: x+y, self.nums)


# # the old trick won't work, take too much time to update. 
# class NumArray(object):
#     def __init__(self, nums):
#         self.nums = nums
#         self.length = len(nums)
#         self.subset_sum = [0]*(self.length+1)
#         self.cal_subset_sum(1)
#         
#     def cal_subset_sum(self, idx):
#         for i in range(idx, self.length+1):
#             self.subset_sum[i] = self.subset_sum[i-1] + self.nums[i-1]
#     
#     def update(self, i, val):
#         self.nums[i] = val
#         self.cal_subset_sum(i+1)
#     
#     def sumRange(self, i, j):
#         return self.subset_sum[j+1]-self.subset_sum[i]
#     

# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
numArray = NumArray(nums)
print numArray.sumRange(0, 2)  #9
numArray.update(1, 2)
print numArray.sumRange(0, 2)  #8