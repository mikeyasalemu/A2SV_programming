from collections import defaultdict

sizeA ,sizeB = map(int, input().split(" "))

dic = defaultdict(list)

# initialize the dictionary by the index of the first word charaters
for index in range(sizeA):
    dic[input()].append(index+1)
    
# print the dictionary values
for index in range(sizeB):
    hold = input() 
    if dic[hold]:
        print(*dic[hold])
    else:
        print(-1)
