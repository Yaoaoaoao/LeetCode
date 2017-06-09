class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # connected component
        m = len(M)
        count = 0
        queue = []
        visited = [False] * m

        def direct_friend(stu):
            return [i for i in range(m) if M[stu][i] == 1 and not visited[i]]

        for stu in range(m):
            if not visited[stu]:
                count += 1
                visited[stu] = True
                queue.extend(direct_friend(stu))
                while len(queue) > 0:
                    next_stu = queue.pop(0)
                    if not visited[next_stu]:
                        visited[next_stu] = True
                        queue.extend(direct_friend(next_stu))
        return count


print Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])  # 2
print Solution().findCircleNum([[1, 1, 0], [1, 1, 1], [0, 1, 1]])  # 1
