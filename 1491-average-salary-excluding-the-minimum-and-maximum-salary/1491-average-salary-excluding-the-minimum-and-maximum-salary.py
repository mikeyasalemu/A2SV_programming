class Solution:
    def average(self, salary: List[int]) -> float:
        
#         find the maximum and minimum values
        min_salary = min(salary)
        max_salary = max(salary)
        ret = 0.0
        size = len(salary)
        
#         and the values other than the max and min to the returned variable
        for values in salary:
            if values != min_salary and values != max_salary and size >= 3:
                ret += values
                
#        divide the value to find the avarage value
        ret = ret / (size -2)
        return ret