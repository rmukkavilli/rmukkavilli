class NextPalindrome {
    public static void main(String args[]) {
        String s = "23143034132";
        String s1 = "1234321";
        String[] testCases = {"1221", "56365", "999", "12321", "89798"};
        for(int i = 0; i<testCases.length; i++) {
        System.out.println(i +"th" + "case" + "o/p for " + testCases[i] + ":: " + getNextMinPalindrome(testCases[i]));
        }
    }

    public static String getNextMinPalindrome(String s) {
        int i = 0;      
        char[] ar = s.toCharArray();
        if (ar.length -1 ==0) return "";
       int mid =  ar.length/2 -1;
       System.out.println("what is the value" + mid + "ar[mid] " + ar[mid]);
        while(mid > i && Integer.parseInt(String.valueOf(ar[mid])) > Integer.parseInt(String.valueOf(ar[mid-1]))) {
            mid--;
        }
        if (Integer.parseInt(String.valueOf(ar[mid+1])) > Integer.parseInt(String.valueOf(ar[mid]))) {
            //System.out.println("what is the value" + ar[mid] + "ar[mid+1] " +ar[mid+1] );
            char temp = ar[mid];
            ar[mid] = ar[mid+1];
            ar[mid+1] = temp;

            char temp_1 = ar[ar.length -1-mid];
            ar[ar.length -1-mid] = ar[ar.length -1-mid-1];
            ar[ar.length -1-mid-1] = temp_1;
        } else  {
            return "";
        }

     return String.valueOf(ar);
    }
}