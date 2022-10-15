class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> b = new ArrayList<Boolean>();
        List<Integer> num = new ArrayList<Integer>();
        int n = 0 , k = 0, j = 0, bl = 0;
   for (int i = 0; i < l.length;i++){
       bl = 0; 
       for(int s = l[i];s <= r[i];s++){
           num.add(nums[s]);
       }
      Collections.sort(num);
         k = 0;
        j = k + 1;
       while( j < num.size()){
           if(k == 0){
             n = num.get(j) - num.get(k);
           }
           else if(num.get(j) - num.get(k) != n){
              bl = 1;
           }
           k++;
           j++;
       }
      if(bl == 0){
          b.add(true);
      } 
       else b.add(false);
       num.clear();
    }     
        return b;
    }
}
