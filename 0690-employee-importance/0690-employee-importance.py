"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # # num = employees
        # lt = employees.id
        self.ans = 0
        # print(employees[id].subordinates)
        # print(len(employees))
        visited = set()
        for i in range(len(employees)):
            if employees[i].id == id:
                return self.calc(employees,i,visited)
                # print(employees[i].subordinates)
        # print()
        # return self.ans
    def calc(self,employees,ind,visited):
        # self.ans+= employees[ind].importance
        visited.add(employees[ind].id)
        if len(employees[ind].subordinates) == 0:
            return employees[ind].importance
        count = 0
        for subordinate in employees[ind].subordinates:
            for i in range(len(employees)):
                if subordinate == employees[i].id and subordinate not in visited:
                    # print(subordinate)
                    count+=self.calc(employees,i,visited)
        return count+employees[ind].importance