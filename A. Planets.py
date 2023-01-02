from collections import Counter
tests = int(input())
for test in range(tests):
    accept = list(map(int, input().split()))
    size = accept[0]
    cost_2 = accept[1]
    lst = list(map(int, input().split()))
    dic  = Counter(lst)
    lst = set(lst)
    counter = 0
    for planets  in lst:
        if dic[planets] > 1:
            if dic[planets] > cost_2:
                counter += cost_2
            
            else:
                counter += dic[planets]  
        else:
            counter += 1
    print (counter)
