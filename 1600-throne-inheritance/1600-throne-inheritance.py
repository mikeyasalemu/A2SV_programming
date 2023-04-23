class ThroneInheritance:
    
    def __init__(self, kingName: str):
        self.dic = defaultdict(list)
        self.kingName = kingName
        self.dead = set()
    def birth(self, parentName: str, childName: str) -> None:
        self.dic[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add((name))

    def getInheritanceOrder(self) -> List[str]:
        self.lst = []
        visited = set()
        if (self.kingName) not in self.dead:
            self.lst.append(self.kingName)
        # print(self.dic)
        def dfs(curr):
            visited.add(curr)
            for i in self.dic[curr]:
                if (i) not in self.dead:
                    self.lst.append(i)
                dfs(i)
                
        dfs(self.kingName)
        return self.lst


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()