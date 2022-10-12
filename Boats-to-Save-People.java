class Solution {
    public int numRescueBoats(int[] people, int limit) {
  ArrayList<Integer> al = new ArrayList<Integer>(); 
        int p = 0;
        while(p < people.length){
            al.add(people[p]);
            p++;
        }
       Collections.sort(al); 
       Integer[] arr = new Integer[al.size()]; 
        arr = al.toArray(arr); 
         int i = 0, j = arr.length -1, n = 0;
      while (i <= j){
           if(arr[i] + arr[j] <= limit){
              i++;  
          }
              n++;
              j--;
              }
   
        return n;
    }
}
