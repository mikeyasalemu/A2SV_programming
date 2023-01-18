size = int(input())
for i in range(size):
    row , column = map(int, input().split())
    matrix = []
    for i in range(0,row):
        matrix.append(list(map(int, input().split())))
        
    #  from right to left sum holder
    rt_lft =[]
    for i in range(row + column -1):
       rt_lft.append(0) 
    for i in range(row):
       for j in range(column):
           rt_lft[i + j]+= matrix[i][j]
   ###############################     
   # from left to right sum holder
    lft_rt = {}
    for i in range(row):
       for j in range(column):
           if lft_rt.get(i -j):
               lft_rt[i-j] += matrix[i][j]
           else:
               lft_rt[i-j] = matrix[i][j]
    #############################
    maxi = float('-inf')
    for i in range(row):
        for j in range(column):
            maxi = max(maxi,  rt_lft[i + j] + lft_rt.get(i -j) - matrix[i][j])
            
    print (maxi)
