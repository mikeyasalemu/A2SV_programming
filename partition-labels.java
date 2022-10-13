class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> num = new ArrayList<Integer>();
        String[] str = s.split("");
        int i = 0, j = str.length - 1, temp =  -1, n = 0, sum = 0; 
        while(i <= str.length - 1){
            //////
            if(str[i].equals(str[j])){ 
                if( temp < j){
                    temp = j;
                }
               else if( j == str.length - 1 ){
                    num.add(temp + 1 - sum );
                    break;
               }
                else if( i == temp){
                    i = temp + 1;
                    if( n == 0){
                         num.add(temp + 1);
                    }
                    else
                    num.add(temp - sum + 1);
                     n++;
                    sum += num.get(n - 1);
                    j = str.length-1;
                }
               else if(i != temp) {
                   i++;
                j = str.length-1;
               }
            }
            /////////
            else if(!str[i].equals(str[j]) &&  i == j){
                 i = temp + 1;
                    if( n == 0){
                         num.add(temp + 1);
                    }
                    else
                         num.add(temp - sum + 1);
                          n++;
                         sum += num.get(n - 1);
                  j = str.length-1;
                }
            else
                j--;
        }
        
        return num;
        
    }
}
