
class StringCompression {

    public static void main(String args[]) {
        String a = "aaaaaaaaaaaaaaaaaaa";
        char[] ar = a.toCharArray();
        System.out.println(stringCompress(ar));
    }

    public static int stringCompress(char[] ar) {
        int i = 0;
        int count = 0;
        int left = 0;
        int j = 0;
        int w = 0;
        int right = ar.length;
        while (i < right) {
            j = i;
            while (j < right && (ar[i] == ar[j])) j++;
            count = j - i;

            if (count > 1) {
                w = i;
                for (char c : String.valueOf(count).toCharArray()) {
                    ar[w++] = c;

                }

            }
            i = j;

        }
        return w;
    }
}
