class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        from collections import defaultdict
        processes = defaultdict(list)
        for i in range(len(pid)):
            processes[ppid[i]].append(pid[i])
        
        rst = set()
        queue = processes.get(kill, [])
        rst.add(kill)
        while len(queue) > 0:
            pkill = queue.pop(0)
            if pkill not in rst:
                rst.add(pkill)
                queue.extend(processes[pkill])
        return list(rst)
        
print Solution().killProcess([1,3,10,5], [3,0,5,3], 5)
print Solution().killProcess([1,3,10,5], [3,0,5,3], 3)
print Solution().killProcess([1], [0], 1)