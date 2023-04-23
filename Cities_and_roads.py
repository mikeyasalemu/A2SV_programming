size = int(input())
lst = []
for i in range(size):
   lst.append(list(map(int, input().split())))
ans = 0
for i in range(size):
    for j in range(size):
        if lst[i][j] == 1:
            ans+=1
            
print(ans//2)