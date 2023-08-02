class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        st = []
       
        def rec(ind, arr):
            if ind < len(s) and len(arr) == 4:
                    return
            if ind > len(s) or len(arr) > 4:
                return 
            if ind == len(s):
                if len(arr) == 4:
                    print("yes",arr)
                    st.append('.'.join(arr))
                return
           
            
            if s[ind] == '0':
                arr.append('0')
                rec(ind + 1, arr)
                arr.pop()
            else:
                for i in range(ind+1, len(s)+1):
                    if 0 <= (int(s[ind:i]))<= 255:
                        arr.append(s[ind:i])
                        rec(i, arr)
                        arr.pop()
                    else:
                        return
                

        rec(0, [])
        # print(st)
        return st