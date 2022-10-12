class Solution {
    public String sortSentence(String s) {
        String arr[] = s.split(" ");
        String ans[] = new String[arr.length];
        StringBuffer sb = new StringBuffer();
        for (String ch: arr) {      
            int b = Character.getNumericValue(ch.charAt(ch.length()-1));
            ans[b-1] = ch.substring(0,ch.length() - 1);
        }
        for(int i = 0; i < ans.length; i++){
            if(i + 1 != ans.length){
                 sb.append(ans[i] + " ");
            }
            else{
                 sb.append(ans[i]);
            }
          
             
        }
       
        return sb.toString();

    }
}
