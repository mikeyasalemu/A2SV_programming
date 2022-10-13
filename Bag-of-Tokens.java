class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
         ArrayList<Integer> al = new ArrayList<Integer>(); 
        int p = 0;
        while(p < tokens.length){
            al.add(tokens[p]);
            p++;
        }
       Collections.sort(al);
       Integer[] arr = new Integer[al.size()]; 
        arr = al.toArray(arr);        
        int i = 0,j = arr.length-1, s = 0, k = arr.length - 1;      
        while(i < j ){         
            if(s == 0 && arr[i] > power){
               break;
            }
              /// FACE UP
            else if(arr[i] <= power ){
                power -=arr[i]; 
                s++;
                i++;
                 if(i == j && arr[i] <= power ){
                     s++;
                    break;
                }
            }           
            ///FACE DOWN
            else if(s > 0 && i < j){           
                power += arr[j];
                j--;
                s--;    
                 if(i == j && arr[i] <= power ){
                     s++;
                    break;
                }
            }  
        }
        if( i == arr.length - 1 && arr[i] <= power){
                    s++;
                }  
        return s;
    }
}
