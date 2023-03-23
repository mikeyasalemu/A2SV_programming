class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # if n == 1:
        #     return 0
        # if n == 2:
        #     if k == 1:
        #         return 0
        #     return 1
        # print(math.ceil(1//2))/
        check = self.helper(1, 1,n,k)
        if check[1] == True:
            return 1
        return 0
    def helper(self,size,count,n,k):
        if count == n:
            if k > math.ceil(size/2):
                return [abs((size//2) - k), True]
            else:
                return [k, False]
            
        temp = self.helper(size*2,count+1,n,k)
        if size > 1:
            if temp[0] > (size//2):
                    tr = True
                    if temp[1] == True:
                        tr = False
                    return [abs((size//2) - temp[0]), tr]
            else:
                tr = False
                if temp[1] == True:
                        tr = True
                return [temp[0] , tr]
        return [temp[0],temp[1]]