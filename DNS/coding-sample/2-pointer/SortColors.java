import java.util.Arrays;
//print code/sum(wave lenght)threeSum//0

class SortColors {
    public static void main(String args[]) {
        //int[] ar = {2,2,2, 0, 0,1,1,0};
        int[] ar = {2,2,2,1,0,1,0,0};
        System.out.println(Arrays.toString(sortColors(ar)));
    }

    public static int[] sortColors(int[] ar) {
        int left = 0;
        int right = ar.length - 1;
        int i = 0;
        while (i <= right) {
            System.out.println("value of this "+ ar[i] + "i value : "+i);
            if (ar[i] == 0) {
                int temp = ar[i];
                ar[i] = ar[left];
                ar[left] = temp;
                left++;
                i++;
                System.out.println("value of i in 0--> " + i + "right " + right);
                System.out.println("va in 0  " + Arrays.toString(ar) );
            } else if (ar[i] == 2) {
                int temp = ar[i];
                ar[i] = ar[right];
                ar[right] = temp;
                right--;
                System.out.println("value of i in 2-->" + i +"right " + right);
                System.out.println("va in 2  " + Arrays.toString(ar) );
            } else {
                i++;
            }
        }
          return ar;
    }
}