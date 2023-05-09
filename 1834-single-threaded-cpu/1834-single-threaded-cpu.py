class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        i = 0
        for nums in tasks:
            nums.append(i)
            i+=1
        heapify(tasks)
        
        heap = []
        time = -1
        ans = []
        
        while tasks or heap:
            if not heap and tasks[0][0] > time:
                time = tasks[0][0]
                
            while not heap or (tasks and tasks[0][0] <= time): 
                temp = heappop(tasks)
                temp[0],temp[1] = temp[1], temp[0]
                temp[1],temp[2] = temp[2],temp[1]
                heappush(heap,temp)
                
            if heap:
                temp = heappop(heap)
                time+= temp[0]
                ans.append(temp[1])
        
        return ans
                