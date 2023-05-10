class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dic = defaultdict(lambda:1)
        dic2 = defaultdict(set)
        for i in range(len(recipes)):
            dic[recipes[i]]+= len(ingredients[i])
            for i in range(len(ingredients)):
                for ing in ingredients[i]:
                    dic2[ing].add(recipes[i])
        
        for key in dic2.keys():
            dic2[key] = list(dic2[key])
        # print(dic)
        # print(" ",dic2)
        check = set(recipes)
        ans = []
        visited = set()
        key = list(dic2.keys())
        
        def bfs(val):
            temp = queue.popleft()
            
            for rec in dic2[val]:
                dic[rec]-=1
                if dic[rec] == 1:
                    if rec in check:
                        ans.append(rec)
                    queue.append(rec)
                    visited.add(rec)
                    bfs(rec)
                    
        for itm in supplies:
            if itm not in visited:
                queue = deque({itm})
                visited.add(itm)
                bfs(itm)
        # print(ans)     
        return ans