
def helper(pw,k):
    if k == 0:
        return pw
    return helper(k,pw%k)
    
pw, k = map(int,input().split())
if pw != k:
    print(1)
else:
    print(helper(k,pw))