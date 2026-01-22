class ReverseString1 {
    public static void main(String args[]) {
        String s = "coder";
        System.out.println(reverseString1(s));
     }

     public static String reverseString1(String s) {
        char[] ar = s.toCharArray();
        System.out.println("what is teh value "+ ar.length);
        int n = ar.length/2;
        for (int i=0; i< n/2; i++) {
            char temp = ar[i];
            ar[i] = ar[ar.length - i - 1];
            ar[ar.length - i - 1] = temp;

        }

        return String.valueOf(ar);
     }
}