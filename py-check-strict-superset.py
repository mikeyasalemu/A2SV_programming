setA = set(input().split())
num_set = int(input())
lst = []

check = True
for iterate in  range(num_set):
    lst = input().split()
    
    if setA.issuperset(set(lst)) == False:
        check = False
        break
    lst.clear()
print (check)
