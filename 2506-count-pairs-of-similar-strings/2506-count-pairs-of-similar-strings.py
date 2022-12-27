class Solution:
    def similarPairs(self, words: List[str]) -> int:
        size = len(words)
        hold = []
        
        for index in range(size):
            hold = set(sorted(list(words[index])))
            words[index] = str(hold)
        lst = Counter(words)
        print(lst)
        ret = 0
        for index in lst:
            
            if lst[index] > 1:
                ret += int(lst[index] * (lst[index] - 1)/ 2)
        
        
        return ret