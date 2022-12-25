class Solution:
    def average(self, salary: List[int]) -> float:
        
#         find the maximum and minimum and sum of values
        min_salary = min(salary)
        max_salary = max(salary)
        sum_salary = sum(salary)
        
#         then substrack theax and min values from sum 
#         and dividing it to the size - 2to find the avarage 
        ret = (sum_salary - (min_salary + max_salary)) / (len(salary) -2)
        # ret = 0.0
        # size = len(salary)
        
# #         and the values other than the max and min to the returned variable
#         for values in salary:
#             if values != min_salary and values != max_salary and size >= 3:
#                 ret += values
                
#        divide the value to find the avarage value
        # ret = ret / (size -2)
        return ret