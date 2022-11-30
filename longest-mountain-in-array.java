class Solution {
    public int longestMountain(int[] arr) {
        int ans=0,n=arr.length;
        for(int i=1,j=0; i<n; ){            
            while(i<n && arr[i-1]>=arr[i]){
                i++;
                j++;
            }
            while(i<n && arr[i-1]<arr[i]){
                i++;
            }
            int peek=arr[i-1];
            while(i<n && arr[i-1]>arr[i]){
                i++;
            }
            if(i<=n && peek>arr[i-1]) ans = Math.max(ans,i-j);
            
            while(i<n && arr[i-1]==arr[i]){
                i++;
            }
            j=i-1;
        }
        return ans;
    }
}
