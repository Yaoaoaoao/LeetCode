class Solution:
    """
    Run time: 72ms

    key notes:
    1. keep the original index number, sorted the array. 
    2. assume the two numbers are x and y, loop start with the smallest x (track its index with xlow)
    3. for each x,  y must be between x-t and x+t, call them ymin and ymax, 
       simply check all possible y if x and y's index difference is at most k
    4. Optimization:
        a. when x grows, ymin (and ymax) grows as well. which means, if y is too small for current x, it won't work for any bigger x either. 
           smaller y are ignored forever.  (index tracked by ylow)
        b. if y is bigger than ymax, we don't need to check bigger y for current x.
           bigger y are ignored temporarily. 
    """

    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}

    def containsNearbyAlmostDuplicate(self, nums, k, t):

        l = len(nums)
        if l == 1:
            return False

        nums = [(i, ni) for i, ni in enumerate(nums)]
        nums = sorted(nums, key=lambda x: x[1])

        # the two numbers are x and y
        xlow, ylow = 0, 1

        while xlow < ylow and ylow <= l - 1:
            i, j = xlow, ylow
            x, y = nums[i][1], nums[j][1]
            ymin, ymax = x - t, x + t

            if y < ymin:  # find y's lower bound, all smaller y won't work for bigger x
                ylow += 1
            elif y > ymax:  # bigger y won't work for current x
                xlow += 1
            else:  # get y between ymin and ymax

                while j <= l - 1 and nums[j][1] <= ymax:
                    if i != j and abs(nums[i][0] - nums[j][0]) <= k:
                        return True
                    j += 1

                # check finish for current x, move to the next x
                xlow += 1

            # i != j, ylow must be bigger than xlow. 
            if xlow == ylow:
                ylow += 1

        return False


# some test cases    
print Solution().containsNearbyAlmostDuplicate([3, 6, 0, 4], 2, 2)  # true
print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)  # false
print Solution().containsNearbyAlmostDuplicate([1, 2], 0, 1)  #false
