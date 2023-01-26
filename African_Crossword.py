import collections
row, col = map(int, input().split())
grid = []
for i in range(row):
    lst = list(input())
    grid.append(lst)
####################
row_ = []
for i in range(row):
    dic = collections.defaultdict(int)
    row_.append([])
    for j in range(col):
         dic[grid[i][j]] +=1
    for z in range(col): 
        row_[i].append(dic[grid[i][z]])
##############################
col_ = []
for i in range(col):
    dic = collections.defaultdict(int)
    col_.append([])
    for j in range(row):
         dic[grid[j][i]] +=1
    for z in range(row): 
        col_[i].append(dic[grid[z][i]])          
##########################
col_ = list(zip(*col_)) 
string = ""
for i in range(row):
    for j in range(col):
        if row_[i][j] == 1 and col_[i][j] == 1:
                string+=grid[i][j]
print(string)
