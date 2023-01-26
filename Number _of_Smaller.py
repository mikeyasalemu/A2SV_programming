size1, size2 = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
res = []
pointer2 = 0
greater =0
for pointer1 in range(size2):
    while pointer2 < size1:
        if second[pointer1] > first[pointer2]:
             greater +=1
             pointer2 +=1
        else:
             break
    res.append(greater)
print(*res)
