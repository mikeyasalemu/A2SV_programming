class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        high = 0
        for num1, num2 in edges:
            high = max(num1,num2,high)
            dic[num1].append(num2)
            dic[num2].append(num1)
        target = high -1
        ans = 0
        for num,lst in dic.items():
            if len(lst) == target:
                ans = num
                break
        return ans