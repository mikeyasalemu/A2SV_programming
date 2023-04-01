tests = int(input())
for i in range(tests):
    n = int(input())
    temp = 1
    while not n&temp:
        temp<<=1
    if temp >= n:
        check =1
        while  n&check:
            check<<=1
        temp+=check
    print(temp)
