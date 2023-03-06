class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i
        st = []
        seen = set()
        for i in range(len(s)):
            if  s[i] not in seen:
                while st and st[-1] > s[i] and dic[st[-1]] > i:
                    seen.remove(st.pop())
                
                st.append(s[i])
                seen.add(s[i])
                
           
        return "".join(st)