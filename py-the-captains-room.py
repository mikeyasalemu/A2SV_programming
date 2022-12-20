from collections import Counter
num = int(input())
li = list(map(int ,input().split()))
dic = Counter(li)
print(min(dic, key = dic.get))
