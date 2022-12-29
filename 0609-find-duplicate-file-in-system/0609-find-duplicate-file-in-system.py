class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        answer = []
        
#         iterate through every path
        for index in range(len(paths)):
            string = list(paths[index].split())
            
            
#             split the path and the file then append to the dictionary
            for j in range(1,len(string)):
                string2 = string[j].split('(')
                store[string2[1]].append(string[0]+"/"+string2[0])
                
#       print the duplicated files only
        for value in store.values():
       
            if len(value) >1 :
                answer.append(value)
      
        return answer