#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		left = 0
		right = 0
		for i in range(len(arr)):
		    if (right - left + 1) == K or right + 1 == N:
		        new_val = list(reversed(arr[left:right + 1]))
		      #  new_val = arr[left:right + 1:-1]
		      #  print(new_val)
		        arr[left:right + 1] = new_val
		        left = right + 1
		      
		    
		    right += 1
		return arr


#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends