#User function Template for python3
from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        graph = defaultdict(list)
        incomings = defaultdict(int)
        for i in range(N - 1):
            word1 = alien_dict[i]
            word2 = alien_dict[i + 1]
            
            p1, p2 = 0, 0
            while p1 < len(word1) and p2 < len(word2) and word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
            
            if p1 < len(word1) and p2 < len(word2):
                graph[word1[p1]].append(word2[p2])
                incomings[word2[p2]] += 1
                
        visited = set()
        queue = deque()
        answer = []
        for i in range(K):
            if incomings[chr(97 + i)] == 0:
                queue.append(chr(97 + i))
            
        while queue:
            curr = queue.popleft()
            answer.append(curr)
            for adj in graph[curr]:
                incomings[adj] -= 1
                if incomings[adj] == 0:
                    queue.append(adj)
                    
        return "".join(answer)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends