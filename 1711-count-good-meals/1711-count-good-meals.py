class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = defaultdict(int)
        count = 0
        
#       iterate through the list
        for num1 in deliciousness:
            power_num = 1
            
#           maximum it can go is 22 loop
            for _ in range(22): 
                num2 = power_num - num1
            
                if num2 in dic:
#                     num1 can be paiered only upto the number of time  num2  occurs
                    count += dic[num2]
                power_num *=2
            dic[num1] += 1
            
            
        return count % (10**9 + 7)
        