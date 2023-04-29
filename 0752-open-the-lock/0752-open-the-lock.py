class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        direction = ("1000","0100","0010","0001")
        visited = set()
        deadends = set(deadends)
        queue = deque()
        queue.append(("0000", 0))
        visited.add("0000")
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        check = False
        ans = -1
        while queue:
            
            current,val = queue.popleft()
            
            for way in direction:
                
                new_p = ""
                
                for i in range(4):
                    temp = int(way[i])+int(current[i])
                    if temp == 10:
                        temp = 0
                    new_p+= str(temp)
                    
                if new_p == target:
                    check = True
                    ans = val+1
                    break
                    
                if new_p not in visited and new_p not in deadends:
                    queue.append((new_p,val+1))
                    visited.add(new_p)
                    
                new_n = ""   
                
                for i in range(4):
                    temp = int(current[i]) - int(way[i])
                    if temp == -1:
                        temp = 9
                        
                    new_n+=str(temp)
                    
                if new_n == target:
                    check = True
                    ans = val+1
                    break
                    
                if new_n not in visited and new_n not in deadends:
                    queue.append((new_n,val+1))
                    visited.add(new_n)
                    
            if check:
                break
        return ans
                