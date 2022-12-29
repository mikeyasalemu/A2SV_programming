class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        answer = []
        for index in range(len(paths)):
            string = list(paths[index].split())
            
            for j in range(1,len(string)):
                string2 = string[j].split('(')
                store[string2[1]].append(string[0]+"/"+string2[0])
                
        for value in store.values():
            # print(len(value))
            if len(value) >1 :
                answer.append(value)
        # print(answer)
        return answer