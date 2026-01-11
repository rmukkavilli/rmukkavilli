import java.util.Arrays;
class KRotations {
    public static void main(String args[]) {
        int[] nums =  new int[] {1,2,3,4,5};
        int k = 2;
        getKRotations(nums, k);
        System.out.println(Arrays.toString(nums));

    }

    public static void getKRotations(int[] nums, int k) {

         int n = nums.length;
        if (k > n) {
            k = k %n;
        }
     
        for (int i=0; i<n/2;i++) {
            int temp = nums[i];
            nums[i] = nums[n -1 - i];
            nums[n -1 - i]  = temp;
        }
         for (int j=0; j<k/2;j++) {
             int temp_1 = nums[j];
            nums[j] = nums[k -1 - j];
            nums[k -1 - j]  = temp_1;
         }
            System.out.println("k " + k + " <--n/2 " + n/2);
         for (int l = k; l<(n+k)/2; l++) {
            //System.out.println(nums[l] + ": " + nums[n-1 - (l-k-1)]);
             int temp_2 = nums[l];
             nums[l] = nums[n+k -1 -l];
             nums[n+k -1 -l] = temp_2;
         }
        // Write your solution code here
    }
}
