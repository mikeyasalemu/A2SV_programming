size1, size2 = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
index1 = 0
index2 = 0
ans = []
while index1 < size1 and index2 < size2:
    if lst1[index1] < lst2[index2]:
        ans.append(lst1[index1])
        index1 += 1
    else:
        ans.append(lst2[index2])
        index2 += 1
if index1 == size1:
    ans += lst2[index2:]
else:
    ans += lst1[index1:]
print(*ans)
