class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
#       put the players  and the number of matches they lost in the dictionary
        dic = defaultdict(int)
        for winner, loser in matches:
            if winner not in dic:
                    dic[winner] = 0
            dic[loser] +=1

 #     put then in new list according to the given rules   
        win = []
        lost1 = []
        for key, values in dic.items():
            if values == 0:
                win.append(key)
            elif values == 1:
                lost1.append(key)
        return [sorted(win), sorted(lost1)]
            
               
        
