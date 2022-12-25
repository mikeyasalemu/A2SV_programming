class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        ret = 0.0
        size = len(salary)
        for values in salary:
            if values != min_salary and values != max_salary and size >= 3:
                ret += values
        ret = ret / (size -2)
        return ret