class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i in range(len(queries)):
            queries[i] = ''.join(sorted(queries[i]))
        for i in range(len(words)):
            words[i] = ''.join(sorted(words[i]))
        q = []
        w = []
        for i in range(len(queries)):
            temp = queries[i][0]
            freq = 1
            for j in range(1,len(queries[i])):
                if queries[i][j] == temp:
                    freq+=1
                else:
                    break
            q.append(freq)
        for i in range(len(words)):
            temp = words[i][0]
            freq = 1
            for j in range(1,len(words[i])):
                if words[i][j] == temp:
                    freq+=1
                else:
                    break
            w.append(freq)
        w.sort()
        ans = []
        for i in range(len(q)):
            left = 0
            right = len(w) -1
            while left <= right:
                mid = left + (right - left)//2
                if w[mid] > q[i]:
                    right = mid -1
                else:
                    left = mid+1
            ans.append(len(w) - left)
        return ans