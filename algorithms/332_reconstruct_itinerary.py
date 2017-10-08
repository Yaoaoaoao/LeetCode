class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        result = []
        def dfs(a):
            while airports[a]:
                dfs(airports[a].pop())
            result.append(a)
                
        from collections import defaultdict
        airports = defaultdict(list)
        for f, t in sorted(tickets)[::-1]:
            airports[f].append(t)
        dfs('JFK')
        return result[::-1]

        


print Solution().findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
     ["ATL", "SFO"]])
