class MinmovesPalindrome {
    public static void main(String args[]) {
        String s = "mamad";
        System.out.println("minNumOf moves" + minMovesToPalindrome(s));
    }

    public static int minMovesToPalindrome(String s) {
        int moves = 0;
        char[] ar = s.toCharArray();
        int j = ar.length -1;
       for (int i=0; i<ar.length; i++ ) {
            int k = j;
            for(;k>i; k--) {
                 if(ar[i] == ar[k]) {
                    System.out.println("what is teh valie of ar-->  " + ar[i] + " k val  " + ar[k]);
                    for (;k < j;k++) {
                    char temp = ar[k];
                    ar[k] = ar[k+1];
                    ar[k+1] = temp;
                    moves++;
                  }
                  j--; 
                  break;
            }
        }
        if(k==i) {
            moves = ar.length/2 - i;
        }
    } 
    return moves;
}
}