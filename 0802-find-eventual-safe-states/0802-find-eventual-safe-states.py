class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        
        self.visited = set()
        
        self.check = [0]*len(graph)
       
        for i in range(len(graph)):
            
              if self.check[i] == 0:
                    self.check[i] = 2
                    self.dfs(i,graph)
                    
                
        for i in range(len(graph)):
            if self.check[i] == 1:
                ans.append(i)
                
        return ans
    
    
    def dfs(self,val,graph):
        

        if not graph[val]:
            self.check[val] = 1
            return True
        
        check = 0
        self.check[val] = 2
        for i in graph[val]:
            
            if self.check[i] == 1:
                check+=1  
                
            elif self.check[i] == -1 or self.check[i] == 2:
                self.check[i] = -1
                break 
              
            else:
                temp = self.dfs(i,graph)
                if temp:
                    check+=1
                else:
                    break

        if check == len(graph[val]):
            self.check[val] = 1
            return True
        
        self.check[val] = -1    
        
        return False
    
        
        