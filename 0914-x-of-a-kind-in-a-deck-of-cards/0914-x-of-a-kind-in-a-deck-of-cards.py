class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic = Counter(deck)
        num = len(dic.values())
        dic2 = defaultdict(int)
        
        for i in dic.values():
            st = set()
            temp = i * i
            d = 2
            while d * d <= temp:
                
                while temp % d == 0:
                    
                    st.add(d)
                    temp //= d
                    
                d+=1
           
            for val in st:
                dic2[val]+=1
                
        ans = False
        
        for i in dic2.values():
            if i == num:
                ans = True
                break
                
        return ans
