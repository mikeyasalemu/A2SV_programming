size = int(input())
lst = list(map(int, input().split()))
even = False
odd = False
for i in lst:
    if i % 2:
        even = True
    else:
        odd = True
if odd and even:
    lst.sort()
print(*lst)
