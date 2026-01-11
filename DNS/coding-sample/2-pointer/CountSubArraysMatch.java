class CountSubArraysMatch {
    public static void main(String args[]) {
        int[] ar = new int[] {1,3,5,2,7,5};
        int minK = 1;
        int maxk = 5;

        System.out.println(getNumberOfSubArrrays(ar, minK, maxk));
    }

    public static int getNumberOfSubArrrays(int[] ar, int minK, int maxK) {
        int lb  =-1;
        int min_pos = -1;
        int max_pos = -1;
        int count =0;
        for (int i=0; i<ar.length;i++) {
            if(ar[i] == minK) {
                min_pos = i;
            } 

            if (ar[i] == maxK) {
                max_pos= i;
            }

            if (ar[i] < minK || ar[i] > maxK) {
                lb = i;
                min_pos  = -1;
                max_pos = -1;
            }

            if (min_pos != -1 && max_pos != -1) { 
                System.out.println("min_pos " + min_pos + "max_pos " + max_pos + "lb " + lb + "count "+ count +" -->  "+  Math.min(min_pos, max_pos) + "max"  +  (count+ Math.max(lb, Math.min(min_pos, max_pos)) - lb));
                count += (Math.max(0, Math.min(min_pos, max_pos)) - lb);
                System.out.println("what is the count" + count);
            }

        }
            return count;
    }
}