size = int(input())
lst = []
for i in range(size):
   lst.append(list(map(int, input().split())))
st = []
for i in range(size):
    st.append([])
    for j in range(size):
        if lst[i][j] == 1:
            st[-1].append(j+1)
for i in range(len(st)):
    print(len(st[i]), *st[i])