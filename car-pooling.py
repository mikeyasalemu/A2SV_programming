class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = defaultdict(int)
        for cap,fro,to in trips:
            dic[fro] +=cap
            dic[to] -=cap
        pre = 0
        for i in sorted(dic):
            pre += dic[i]
            if pre > capacity:
                return False
        return True