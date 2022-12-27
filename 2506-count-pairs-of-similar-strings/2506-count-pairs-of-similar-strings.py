class Solution:
    def similarPairs(self, words: List[str]) -> int:
        size = len(words)
        hold = []
        
#       give every word character in words with out repeating and in sorted order 
#           to another list 
        for index in range(size):
            hold = set(sorted(list(words[index])))
            words[index] = str(hold)
        lst = Counter(words)
        ret = 0
        
#         using the pairing formula to get the correct number 
        for index in lst:
            
            if lst[index] > 1:
                ret += int(lst[index] * (lst[index] - 1)/ 2)
        
        
        return ret
#     count = 0
#         dic = defaultdict(lambda : 0)
        
#         for i, word in enumerate(words):
#             word = "".join(sorted(set(word)))
#             count += dic[word]
#             dic[word] += 1
         
#         return count