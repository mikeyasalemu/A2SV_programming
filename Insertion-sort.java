import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
    // Write your code here
    //   System.out.println(arr);
    //   System.out.println(n);
        int i = n - 1;
         int L =  arr.get(i);
       for (int j = i - 1; j >= 0; j--) {
           if(L <= arr.get(j))
           {
               arr.set(j + 1, arr.get(j));
               System.out.println(arr.toString().replace("[","").replace("]","").replace(",","") );// to replace unwanted signs
               if( j == 0){ //to avoid java out of bound exception.
                   arr.set(j, L); 
                   System.out.println(arr.toString().replace("[","").replace("]","").replace(",","") );
               }
           }
           else
               {
                   arr.set(j + 1, L); 
                   System.out.println(arr.toString().replace("[","").replace("]","").replace(",","") );
                   break;
               }
           
    }

  } 
 }
// }

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.insertionSort1(n, arr);

        bufferedReader.close();
    }
}
