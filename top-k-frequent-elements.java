class Solution {
    public int[] topKFrequent(int[] nums, int k) {
      Map<Integer, Integer> map = new HashMap<>();
      ArrayList<Integer> list = new ArrayList<Integer>();      
        int i = 0;
        while(i< nums.length){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
            i++;
        }
        for ( int key : map.keySet() ) {           
                list.add(map.get(key));
            }
       Collections.sort(list,  Collections.reverseOrder());
        int[] arr = new int[k];
        int add = 0;
      while(add < k){
        for(Map.Entry<Integer, Integer> entry: map.entrySet()) {
                if(entry.getValue() ==list.get(add)) {
                    arr[add] = entry.getKey();
                    }
                  }
               map.remove(arr[add]);
               add++; 
             }
     return arr;
    }
}
