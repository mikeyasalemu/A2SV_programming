
size, diff = map(int,input().split())
arr = list(map(int,input().split()))
dic = []
for i in range(len(arr)):
    dic.append(tuple([arr[i], i]))

def mergeSort(left, right, arr, diff):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left)//2
    
    left_side = mergeSort(left, mid, arr,diff)
    right_side = mergeSort(mid+1, right, arr,diff)
    # print(left_side,"te", right_side)
    return merge(left_side, right_side,diff)

def merge(lst1, lst2,diff):
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    # print(lst1,"tr",lst2)
    left = 0
    right = 0
    ans = []
    while left < len(lst1) and right < len(lst2):
        if lst1[left][0] < lst2[right][0]:
            if abs(lst1[left][0] - lst2[right][0]) <= diff:
                break
            left+=1
        else:
            if abs(lst1[left][0] - lst2[right][0]) <= diff:
                break
            right+=1
    while left < len(lst1):
        ans.append(lst1[left])
        left+=1
    while right < len(lst2):
        ans.append(lst2[right])
        right+=1
    
    return ans

temp = mergeSort(0,len(dic) -1 ,dic, diff)
ans = []
for i in temp:
    ans.append(i[1]+1)
ans.sort()
print(*ans)