class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
         dic = Counter(s)
         for x in t:
                if dic.get(x):
                    dic[x] -= 1
                else:
                    return x