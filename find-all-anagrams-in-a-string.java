class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        if(p.length() > s.length()){
            return list;
        }
        ///////////////////
        for(int i = 0; i < p.length();i++){
            map.put(p.charAt(i), map.getOrDefault(p.charAt(i), 0) + 1);
        }
        ////////////////////////
        for(int i = 0; i < p.length();i++){
            map2.put(s.charAt(i), map2.getOrDefault(s.charAt(i), 0) + 1);
            
            if(map.equals(map2)){
                list.add(0);
            }
        }
        
        int right = p.length(), left = 0;
        while(right <  s.length()){
            
             map2.put(s.charAt(right), map2.getOrDefault(s.charAt(right), 0) + 1);
            
             map2.replace(s.charAt(left), map2.get(s.charAt(left) ) -1);
                if (map2.get(s.charAt(left)) == 0){
                   map2.remove(s.charAt(left)); 
                } 
                left++;
                right++;
             if(map.equals(map2)){
                list.add(left);
            }
            
        }
        
        return list;
    }
}
