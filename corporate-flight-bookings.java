class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
       int[] arr = new int[n];
       int i = 0;
       int j = 0;
        while( i < bookings.length){
            
             j = bookings[i][0] - 1;
            
            while( j < bookings[i][1]){
                
                 arr[j] += bookings[i][2];
                 j++;
               }
            i++;
        }
        return arr;
    }
}
