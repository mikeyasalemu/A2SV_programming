from collections import Counter
num = int(input())
li = list(map(int ,input().split()))
dic = Counter(li)
print(min(dic, key = dic.get))

"""num = int(input())
li = list(map(int ,input().split()))
dic = dict()
for x in li:
    dic[x] = 1 + dic.get(x , 0)
for key,val in dic.items():
    if value == 1:
        print (key)"""
