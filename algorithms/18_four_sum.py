class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def fourSum(self, nums, target):
        n = sorted(nums)
        l = len(nums)
        rtn = []
        
        for a in xrange(l-3):
            # add restriction to accelerate 
            if n[a] > target/4:
                break
            if a>0 and n[a] == n[a-1]:
                continue
                
            for b in xrange(a+1, l-2):
                # add restriction to accelerate 
                if n[b] > (target-n[a])/3:
                    break
                if b>a+1 and n[b] == n[b-1]:
                    continue
                    
                c = b+1
                d = l-1
                # add restriction to accelerate 
                if n[c] > (target-n[a]-n[b])/2 or n[d] < (target-n[a]-n[b])/2:
                    continue
                
                while c<d:
                    sum_ = n[a]+n[b]+n[c]+n[d]
                    if sum_ == target:
                        rtn.append((n[a], n[b], n[c], n[d]))
                    
                    if sum_-target > 0: # d too large
                        d -= 1
                    else:
                        c += 1

        return map(list, list(set(rtn)))


print Solution().fourSum([0,0,0,0], 0)
print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print Solution().fourSum([-1,0,1,2,-1,-4], -1)
# print Solution().fourSum([-497,-473,-465,-462,-450,-445,-411,-398,-398,-392,-382,-376,-361,-359,-353,-347,-329,-328,-317,-307,-273,-230,-228,-227,-217,-199,-190,-175,-155,-151,-122,-102,-97,-96,-95,-87,-85,-84,-73,-71,-51,-50,-39,-24,-19,-1,-1,7,22,25,27,37,40,43,45,51,72,91,97,108,119,121,122,123,127,156,166,171,175,180,203,211,217,218,224,231,245,293,297,299,300,318,326,336,353,358,376,391,405,423,445,451,459,464,471,486,487,488], 2251)

