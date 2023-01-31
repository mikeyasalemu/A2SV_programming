cases = int(input())
for i in range(cases):
    size = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    check = True
    for i in range(size - 1):
        if abs(lst[i] - lst[i+1]) > 1:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
