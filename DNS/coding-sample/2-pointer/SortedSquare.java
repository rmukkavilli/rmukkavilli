import java.util.Arrays;
class SortedSquare {
    public static void main(String args[]) {
        int[] ar = {-7, -3, 2,3,11};
        System.out.println(Arrays.toString(findSqureSortedArray(ar)));
    }

    public static int[] findSqureSortedArray(int[] ar) {
        int left = 0;
        int right = ar.length -1;
        int pos = ar.length-1;
        int[] res = new int[ar.length];
        while(left <= right) {
        if (Math.abs(ar[left]) < Math.abs(ar[right])) {
            res[pos] = Math.abs(ar[right] * ar[right]);
            right--;
            pos--;
        } else {
            res[pos] = Math.abs(ar[left] * ar[left]);
            left++;
            pos--;
        }
        }

        return res;
    }
}