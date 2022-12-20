num = int(input())
word = []
for x in range(num):
    word.append(input())

dic = dict()
for i in word:
    dic[i] = 1 + dic.get(i , 0)
print (len(dic) )
print (*dic.values())
