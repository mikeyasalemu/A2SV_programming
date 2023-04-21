from collections import defaultdict
nodes = int(input())
opr = int(input())
dic = defaultdict(list)
for i in range(opr):
    st = list(map(int, input().split()))
    if st[0] == 1:
        dic[st[1]].append(st[2])
        dic[st[2]].append(st[1])
    else:
        print(*dic[st[1]])