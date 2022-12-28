class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for winner, loser in matches:
            if winner not in dic:
                    dic[winner] = 0
            dic[loser] +=1
       
        win = []
        lost1 = []
        for key, values in dic.items():
            if values == 0:
                win.append(key)
            elif values == 1:
                lost1.append(key)
        return [sorted(win), sorted(lost1)]
            
               
        
