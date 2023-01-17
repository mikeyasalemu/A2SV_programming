class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        lst = []
        for key, value  in dic.items():
            lst.append([key, value])
        lst.sort(key = lambda x:(x[1],-x[0]))
        ans = []
        for i in range(len(lst)):
            for  j in range(lst[i][1]):
                ans.append(lst[i][0])
        return ans
        