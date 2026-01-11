class MaxValue {
    public static void main(String args[]) {
        int[] ar = new int[] {1,4,5,8,9,15};
        int[] ar1 = new int[] {2,3,5,7,9,10};
        System.out.println(getMaxValue(ar, ar1));
    }

    public static int getMaxValue(int[] ar, int[] ar1) {
       int p1 = 0;
       int len1 = ar.length;
       int sub_path1 = 0;
       int p2 = 0;
       int len2 = ar1.length;
       int sub_path2 = 0;
        while(p1 < len1 || p2 < len2) {
            if(p1 < len1 && (p2 == len2 || ar[p1] < ar1[p2])) {
                sub_path1 +=ar[p1++];
                System.out.println("first level" + sub_path1 + "ar[p1] " + ar[p1]);
            } else if (p2 < len2 && (p1 == len1 || ar[p1] > ar1[p2])) {
                sub_path2 +=ar1[p2++];
                System.out.println("second level" + sub_path2 + "ar1[p2++] " + ar1[p2++]);
            } else {
                //System.out.println("p1 value " + ar[p1]);
                sub_path1 = sub_path2 = Math.max(sub_path1, sub_path2) + ar[p1];
               // System.out.println(sub_path1);
            p1++;
            p2++;
            }
      
       }
       return Math.max(sub_path1, sub_path2);
}
}