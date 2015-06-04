class Solution:
    """
    # 0m0.475s
    just check Sieve_of_Eratosthenes: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    count only less than n
    1 is not a prime number
    """
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        a = [True] * (n+1)
        a[0], a[1] = False, False
        for i in xrange(2, int(n**0.5)+1):
            if a[i]:
                j = i**2
                while j <= n:
                    a[j] = False
                    j += i
        # don't count last one, the question ask less than n
        a.pop(-1) 
        return a.count(True)


# print Solution().countPrimes(0) # 0
# print Solution().countPrimes(1) # 0
# print Solution().countPrimes(2) # 0
# print Solution().countPrimes(3) # 1
# print Solution().countPrimes(4) # 2
print Solution().countPrimes(1500000)