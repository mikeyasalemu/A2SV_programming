class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        dic2 = defaultdict(deque)
        
        check = set()
        for num1 , num2 in prerequisites:
            dic[num2].append(num1)
            dic2[num1].append(num2)
            
            
        visited = set()
        
        ans  = []
        for i in range(numCourses):
            if i not in visited and not dic2[i]:
                queue = deque([i])
                
                visited.add(i)
                while queue:
                    temp = queue.popleft()
                    ans.append(temp)
                    
                    for val in dic[temp]:
                        if val not in visited:
                            if  dic2[val]:
                                dic2[val].pop()
                                
                            if not dic2[val]:
                                queue.append(val)
                                visited.add(val)
        # print(ans)
        if len(ans) != numCourses:
            return False
        return True