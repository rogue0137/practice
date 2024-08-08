# 690. Employee Importance
# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def BFS(self, employee):

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance_value = 0

        for employee in employees:
            if employee.id == id:
                

        return importance_value
# [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
"""
    [EmployeeID, ImportanceScore, [EmployeeA ... EmployeeN]]
[
    [1, 5, [2, 3], 
    [2, 3, []], 
    [3, 3, []]]
"""

        