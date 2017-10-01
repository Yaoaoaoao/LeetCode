"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        stack = [id]
        total = 0
        while len(stack) > 0:
            e = stack.pop(0)
            stack.extend(employees[e-1].subordinates)
            total += employees[e-1].importance
        return total