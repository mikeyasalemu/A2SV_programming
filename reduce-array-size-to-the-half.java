class Solution {
    public int minSetSize(int[] arr) {
        int size = arr.length;
        Map<Integer, Integer> map= new HashMap<>();
        
        for(int i : arr){
            map.put(i , map.getOrDefault(i , 0) + 1);
            
        }
        
        int freq[] = new int[map.size()];
		
		int indx = 0;
        
		for(int key : map.keySet()) {
			freq[indx] = map.get(key);
			indx++;
		}
		
		Arrays.sort(freq);
        
		if(size % 2 != 0) size+=1; 
        
        int ret = 0, sum = 0;
        
        for( int itr = freq.length - 1; itr >= 0; itr--){
            
           sum+= freq[itr];
           ret++;
           if(sum >= size / 2 )
              break;
       }
      return ret;  
    }
}
