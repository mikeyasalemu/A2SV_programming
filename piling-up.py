# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case = int(input())

#  loop cases
for cases in range(test_case):
    size = int(input())
    nums = list(map(int, input().split()))
    check = "Yes"
    prev_num = max(nums)
    right = size -1
    left = 0
    # compare numers in left to right 
    while right >= left:
        if nums[right] >= nums[left]:
            hold_num = nums[right]
            right-= 1
        else:
            hold_num = nums[left]
            left+= 1 
            
        # check with the previous number
        if prev_num >= hold_num:
            prev_num = hold_num
        else:
            check = "No"
            break
        
    print(check)
