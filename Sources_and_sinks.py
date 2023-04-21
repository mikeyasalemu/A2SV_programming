size = int(input())
lst = []
for i in range(size):
   lst.append(list(map(int, input().split())))
st = list(zip(*lst))
ans1 = []
for i in range(size):
    if 1 not in set(lst[i]):
        ans1.append(i+1)
ans2 = []
for i in range(size):
    if 1 not in set(st[i]):
        ans2.append(i+1)
print(len(ans2), *ans2)
print(len(ans1), *ans1)