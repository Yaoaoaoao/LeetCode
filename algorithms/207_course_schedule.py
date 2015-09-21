class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses:
            return True
        if len(prerequisites) == 0:
            return True
        # topological sort with DFS: find cycle
        from collections import defaultdict
        taken = [False for i in range(numCourses)]
        # False - not visit, True has visited
        requirement = defaultdict(list)
        for course, prereq in prerequisites:
            requirement[course].append(prereq)
        
        for i in range(numCourses):
            if not self.dfs(i, taken, requirement):
                return False
        return True
    
    def dfs(self, course, taken, requirement):
        # none means current node is in the same cycle
        if taken[course] == None:
            return False
        if taken[course]:
            return True
        taken[course] = None
        for j in requirement[course]:
            if not self.dfs(j, taken, requirement):
                return False
        taken[course] = True
        return True
        
            
print Solution().canFinish(2, [[1,0],[0,1]])
print Solution().canFinish(1, [])
print Solution().canFinish(3, [[0,1],[0,2],[1,2]])
            
    