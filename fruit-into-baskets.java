class Solution {
    public int totalFruit(int[] fruits) {
         int n = fruits.length;
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int right = 0;
              while(right < n){
             map.put(fruits[right], map.getOrDefault(fruits[right], 0) + 1);         
           if(map.size() > 2){
             map.put(fruits[left], map.get(fruits[left]) - 1);
                if (map.get(fruits[left]) == 0)
                    map.remove(fruits[left]);
                left++;
           }
           ++right;
        }
        return right - left;        
    }
}
