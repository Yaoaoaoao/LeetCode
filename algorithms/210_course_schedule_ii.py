class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        """
        Nodes: 0 to n-1
        Edges: prerequisites - directed edge.
        Topological sorting
        """
        from collections import defaultdict
        visited,edges = {}, defaultdict(list)
        for course in range(numCourses):
            visited[course] = False
        for pre in prerequisites:
            edges[pre[0]].append(pre[1])
        result = []
        for n in visited.keys():
            if not self.dfs(visited, edges, n, result):
                return []
        return result
        
    def dfs(self, visited, edges, n1, result):
        if visited[n1] == 'visited':
            return False
        elif visited[n1] == 'finished':
            return True
        visited[n1] = 'visited'
        for n2 in edges[n1]:
            if not self.dfs(visited, edges, n2, result):
                return False
        visited[n1] = 'finished'
        result.append(n1)
        return True
        
        
print Solution().findOrder(2, [[0,1]])
print Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print Solution().findOrder(4, [[0,1],[3,1],[1,3],[3,2]])