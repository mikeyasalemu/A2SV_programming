size, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = -1
if k < size:
    if k ==0:
        ans = lst[0] -1
                
    elif lst[k -1] != lst[k]:
        ans = lst[k -1]
    
elif k == size:
    ans = lst[k -1]

if ans == 0:
    ans = -1
print(ans)
