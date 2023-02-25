class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        left = 0
        ans = 0
        for i in range(len(fruits)):
            dic[fruits[i]] +=1
            if len(dic) > 2:
                while len(dic) > 2:
                    dic[fruits[left]] -=1
                    if dic[fruits[left]] == 0:
                        dic.pop(fruits[left])
                    left+=1
            ans = max(ans, i - left+1)
        
        return ans
            
        
        